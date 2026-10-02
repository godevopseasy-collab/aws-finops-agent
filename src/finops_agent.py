import boto3
import datetime
from utils.aws_cost_explorer import get_daily_costs
from analysis.summary_generator import generate_summary
from utils.notifier import send_notification

def main():
    # Define time window (last 7 days)
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=7)

    print(f"Fetching AWS costs from {start_date} to {end_date}...")

    # Step 1: Query AWS Cost Explorer
    costs = get_daily_costs(start_date, end_date)

    # Step 2: Generate human-readable summary
    summary = generate_summary(costs)

    # Step 3: Print locally (logs)
    print(summary)

    # Step 4: Send to Slack/Teams (optional)
    send_notification(summary)

if __name__ == "__main__":
    main()
