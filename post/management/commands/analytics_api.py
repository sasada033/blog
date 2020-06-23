"""Hello Analytics Reporting API V4."""

import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.path.join(BASE_DIR, 'client_secrets.json')
VIEW_ID = settings.VIEW_ID


def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
      An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
      The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [{
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '2020-7-01', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:pageviews'}],
                'dimensions': [{'name': 'ga:pagePath'}],
                'dimensionFilterClauses': [{
                    'filters': [{'dimensionName': 'ga:pagePath', 'expressions': ['/detail/']}]
                }],
                'orderBys': [{'fieldName': 'ga:pageviews', 'sortOrder': 'DESCENDING'}]
            }]
        }
    ).execute()


def get_response():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)

    return response


def get_trend_articles():
    response = get_response()
    for report in response.get('reports', []):
        rows = report.get('data', {}).get('rows', [])
        for row in rows:
            pk = row['dimensions'][0][8:][:-1]
            page_view = row['metrics'][0]['values'][0]
            yield pk, int(page_view)


def print_response():
    """Parses the Analytics Reporting API V4 response."""
    for pk, page_view in get_trend_articles():
        print(pk, page_view)


def main():
    get_trend_articles()
    print_response()


if __name__ == '__main__':
    main()
