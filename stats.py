import plotly.express as px

def calculate_request_type_chart(df):
    """
    Creates a pie chart, showing the spread of different request types used by all companies
    """

    rq_type_dict = df["Request Type"].value_counts().to_dict()

    fig = px.pie(values=list(rq_type_dict.values()), names=list(rq_type_dict.keys()),
                 title='Spread of web form vendor solutions'
                 )

    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.write_html("pie.html")
    #fig.show()


def calculate_framework_chart(df):
    """
     Creates a bar chart, showing the count of companies that mention a privacy framework across all collected privacy policies
    """

    framework_count_dict = {
        "CCPA"  : df["CCPA"].value_counts().to_list(), # count of checkmarks
        "CPA"   : df["CPA"].value_counts().to_list(),
        "CTDPA" : df["CTDPA"].value_counts().to_list(),
        "CDPA"  : df["CDPA"].value_counts().to_list(),
        "UCPA"  : df["UCPA"].value_counts().to_list()
    }

    keys = list(framework_count_dict.keys())
    values = [i for sublist in framework_count_dict.values() for i in sublist]

    fig = px.bar(x=keys, y=values,
                 title="Number of companies that mention privacy frameworks")#, text_auto=True)

    fig.update_layout(
        title_text="Number of companies that mention privacy frameworks",  # title of plot
        xaxis_title_text='Privacy Framework',  # xaxis label
        yaxis_title_text='# of companies',  # yaxis label
    )

    fig.write_html("bar.html")
    #fig.show()