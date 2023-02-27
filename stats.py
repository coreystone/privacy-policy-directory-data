import plotly.express as px

def calculate_request_type_chart(df):
    """
    Creates a pie chart, showing the spread of different request types used by all companies
    """

    rq_type_dict = df["Request Type"].value_counts().to_dict()

    fig = px.pie(values=list(rq_type_dict.values()), names=list(rq_type_dict.keys()),
                 title='How companies let you exercise your data rights'
                 )

    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.write_html("pie.html")
    fig.show()


def calculate_framework_chart(df):
    """
     Creates a bar chart, showing the count of companies that mention a privacy framework across all collected privacy policies
    """

    framework_count_dict = {
        "CCPA": df["CCPA"].value_counts()[":heavy_check_mark:"],  # count of checkmarks
        "CPA": df["CPA"].value_counts()[":heavy_check_mark:"],
        "CTDPA": df["CTDPA"].value_counts()[":heavy_check_mark:"],
        "CDPA": df["CDPA"].value_counts()[":heavy_check_mark:"],
        "UCPA": df["UCPA"].value_counts()[":heavy_check_mark:"]
    }

    keys = list(framework_count_dict.keys())
    values = list(framework_count_dict.values())

    fig = px.bar(x=keys, y=values, text_auto=True,
                 title="Number of companies that mention privacy frameworks")

    fig.update_layout(
        title_text="Number of companies that mention privacy frameworks",
        xaxis_title_text='Privacy Framework',
        yaxis_title_text='# of companies',
    )

    fig.write_html("bar.html")
    fig.show()