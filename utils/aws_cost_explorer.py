import boto3

def get_daily_costs(start_date, end_date):
    ce = boto3.client("ce")
    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.strftime("%Y-%m-%d"),
            "End": end_date.strftime("%Y-%m-%d")
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"]
    )
    return response["ResultsByTime"]
