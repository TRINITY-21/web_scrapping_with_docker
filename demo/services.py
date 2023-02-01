import io
import xlsxwriter


def generate_excel_sheet(input_data, by_year, by_country, by_sector):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    # Creating worksheet
    data_sheet = workbook.add_worksheet(name="Data sheet")
    chart_sheet = workbook.add_worksheet(name="Chartsheet")
    hidden_sheet = workbook.add_worksheet(name="aggregation")

    # Adding formatting
    date_format = workbook.add_format({"num_format": "d-mm-yyyy", "align": "left"})
    dropdown_format = workbook.add_format(
        {"bg_color": "red", "bold": True, "align": "right", "font_color": "white"}
    )
    amount_format = workbook.add_format({"num_format": "€#,##0.00", "align": "left"})
    format_amount_table = workbook.add_format(
        {"num_format": "€#,##0.00", "align": "left", "font_size": 11}
    )

    # adding the scraped data to (Datasheet)
    input_data_table = [
        [
            data.signature_date,
            data.title,
            data.country.name,
            data.sector.name,
            data.signed_amount
        ]
        for data in input_data
    ]

    data_sheet.add_table(
        f"A1:E{len(input_data_table)}",
        {
            "data": input_data_table,
            "columns": [
                {"header": "DATE", "format": date_format},
                {"header": "TITLE"},
                {"header": "COUNTRY"},
                {"header": "SECTOR"},
                {"header": "SIGNED AMOUNT", "format": amount_format},
            ],
        },
    )

    # Adding ChartSheet Dropdown list
    chart_sheet.data_validation(
        "C2",
        {
            "validate": "list",
            "source": ["By Country", "By Year", "By Sector"],
        },
    )
    # Adding default value to the cell
    chart_sheet.write("C2", "By Country", dropdown_format)

    # Adding chart
    chart = workbook.add_chart({"type": "column"})

    # data for hidden sheet to be used for the chart series
    agg_by_year = [
        [data["signature_date__year"], data["total_amount"], data["count"]]
        for data in by_year
    ]
    agg_by_country = [
        [data["country__name"], data["total_amount"], data["count"]]
        for data in by_country
    ]

    agg_by_sector = [
        [data["sector__name"], data["total_amount"], data["count"]]
        for data in by_sector
    ]

    hidden_sheet.add_table(
        f"C1:E{1+len(agg_by_year)}",
        {
            "data": agg_by_year,
            "name": "DataAggregationbyyear",
            "columns": [
                {"header": "Year"},
                {"header": "Signed Amount", "format": format_amount_table},
                {"header": "Quantity"},
            ],
        },
    )

    hidden_sheet.add_table(
        f"G1:I{1+len(agg_by_country)}",
        {
            "data": agg_by_country,
            "name": "DataAggregationbycountry",
            "columns": [
                {"header": "Country"},
                {"header": "Signed Amount", "format": amount_format},
                {"header": "Quantity"},
            ],
        },
    )

    hidden_sheet.add_table(
        f"K1:M{1+len(agg_by_sector)}",
        {
            "data": agg_by_sector,
            "name": "DataAggregationbySector",
            "columns": [
                {"header": "Country"},
                {"header":"Signed Amount", "format": amount_format},
                {"header": "Quantity"},
            ],
        },
    )

    # Creating dynamic data (excel formula) to be used for the chart series as defined names
    chart_y_series = f'=IF(Chartsheet!$C$2="By Country",\
        aggregation!$H$2:$H${1+len(by_country)},\
            IF(Chartsheet!$C$2="By Year",\
                aggregation!$D$2:$D${1+len(by_year)},\
                aggregation!$L$2:$L${1+len(by_sector)}\
            )\
        )'
    chart_x_label = f'=IF(Chartsheet!$C$2="By Country",\
        aggregation!$G$2:$G${1+len(by_country)},\
            IF(Chartsheet!$C$2="By Year",\
                aggregation!$C$2:$C${1+len(by_year)},\
                aggregation!$K$2:$K${1+len(by_sector)}\
            )\
        )'

    workbook.define_name("chart_series", chart_y_series)
    workbook.define_name("chart_labels", chart_x_label)

    # Adding chart series
    chart.add_series(
        {
            "values": "=aggregation!chart_series",
            "categories": "=aggregation!chart_labels",
            "fill": {"color": "#9900ff"},
        }
    )

    # setting addition info
    chart.set_size({"width": 750})
    chart.set_title({"name": "Loans Chart Analysis"})
    chart.set_style(30)

    # Inserting the charts into the chart sheet
    chart_sheet.insert_chart("D6", chart)

    # auto fitting the cells to the width of the contents
    chart_sheet.autofit()
    data_sheet.autofit()

    # Hide the sheet
    hidden_sheet.hide()

    workbook.close()
    output.seek(0)

    return output