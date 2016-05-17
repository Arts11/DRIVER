import subprocess

from django.conf import settings

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def forecast_segment_incidents(segments_csv, output_path):
    """Run R analysis script to output predicted accident counts for each segment

    Args:
        segments_csv (string): Absolute path to a CSV with segments for the forecast script
        output_path (string): Absolute path to a file to write forecasts to (include filename)
    Returns:
        Path of forecast file generated by the R script
    """
    cmd = ['docker',
           'run',
           '--rm',
           '--volumes-from',
           'driver-celery',
           'quay.io/azavea/driver-analysis',
           'Rscript',
           'blackspot_model.R',
           '--outputfile',
           output_path,
           segments_csv]
    subprocess.check_call(cmd)
    return output_path
