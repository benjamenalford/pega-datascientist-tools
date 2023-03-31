import sys
import os

sys.path.append("python")
from pdstools import ADMDatamart, datasets
import pytest

@pytest.fixture
def sample():
    return datasets.CDHSample()

def testHealthCheckRunsWithoutErrors(sample):
    sample.generateHealthCheck(verbose=True)

def testHealthCheckRunsWithoutTables(sample):
    sample.generateHealthCheck(include_tables=False)

def testAdditionalTables(sample):
    sample.exportTables()
    os.remove("Tables.xlsx")
    
@pytest.fixture
def sample_without_predictorbinning():
    return ADMDatamart(
        path="data",
        model_filename="Data-Decision-ADM-ModelSnapshot_pyModelSnapshots_20210526T131808_GMT.zip",
        predictor_filename=None,
    )


def testHealthCheckModelRunsWithoutErrors(sample_without_predictorbinning):
    sample_without_predictorbinning.generateHealthCheck(verbose=True, model_data=True)


def testAdditionalTablesModel(sample_without_predictorbinning):
    sample_without_predictorbinning.exportTables(file="ModelTables.xlsx")
    os.remove("ModelTables.xlsx")
    
def remove_healthCheck():
    os.remove("ADM_HealthCheck.html")