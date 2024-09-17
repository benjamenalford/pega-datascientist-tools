import pathlib
import sys

from pandas import ExcelFile

basePath = pathlib.Path(__file__).parent.parent.parent
sys.path.append(f"{str(basePath)}/python")
import pytest
from pdstools import ADMDatamart, datasets


@pytest.fixture
def sample():
    return datasets.cdh_sample()


@pytest.fixture
def sample_without_predictorbinning():
    return ADMDatamart(
        path=f"{basePath}/data",
        model_filename="Data-Decision-ADM-ModelSnapshot_pyModelSnapshots_20210526T131808_GMT.zip",
        predictor_filename=None,
    )


def test_GenerateHealthCheck(sample):
    hc = sample.generate_health_check(verbose=True)
    assert hc == pathlib.Path("./HealthCheck.html").resolve()
    assert pathlib.Path(hc).exists()
    pathlib.Path(hc).unlink()
    assert not pathlib.Path(hc).exists()


def test_ExportTables(sample):
    excel = sample.exportTables(predictorBinning=True)
    assert excel == "Tables.xlsx"
    assert pathlib.Path(excel).exists()
    spreadsheet = ExcelFile(excel)
    assert list(spreadsheet.sheet_names) == [
        "modeldata_last_snapshot",
        "predictor_last_snapshot",
        "predictorbinning",
    ]
    # TODO we could go further and check the size of the sheets
    # spreadsheet = read_excel(excel, sheet_name=None)
    pathlib.Path(excel).unlink()
    assert not pathlib.Path(excel).exists()


def test_ExportTables_NoBinning(sample):
    excel = sample.exportTables(predictorBinning=False)
    assert excel == "Tables.xlsx"
    assert pathlib.Path(excel).exists()
    spreadsheet = ExcelFile(excel)
    assert list(spreadsheet.sheet_names) == [
        "modeldata_last_snapshot",
        "predictor_last_snapshot",
    ]
    # TODO we could go further and check the size of the sheets
    # spreadsheet = read_excel(excel, sheet_name=None)
    pathlib.Path(excel).unlink()
    assert not pathlib.Path(excel).exists()


def test_GenerateHealthCheck_ModelDataOnly(sample_without_predictorbinning):
    hc = sample_without_predictorbinning.generate_health_check(
        name="MyOrg", verbose=True, modelData_only=True
    )
    assert hc == pathlib.Path("./HealthCheck_MyOrg.html").resolve()
    assert pathlib.Path(hc).exists()
    pathlib.Path(hc).unlink()
    assert not pathlib.Path(hc).exists()


def test_ExportTables_ModelDataOnly(sample_without_predictorbinning):
    excel = sample_without_predictorbinning.exportTables(
        file="ModelTables.xlsx", predictorBinning=True
    )
    assert excel == "ModelTables.xlsx"
    assert pathlib.Path(excel).exists()
    spreadsheet = ExcelFile(excel)
    assert list(spreadsheet.sheet_names) == [
        "modeldata_last_snapshot",
    ]
    # TODO we could go further and check the size of the sheets
    # spreadsheet = read_excel(excel, sheet_name=None)
    pathlib.Path(excel).unlink()


def test_GenerateModelReport(sample):
    report = sample.generate_model_reports(
        name="MyOrg",
        model_list=["bd70a915-697a-5d43-ab2c-53b0557c85a0"],
        only_active_predictors=True,
    )
    expected_path = pathlib.Path(
        "ModelReport_MyOrg_bd70a915-697a-5d43-ab2c-53b0557c85a0.html"
    ).resolve()
    assert report == expected_path
    assert pathlib.Path(report).exists()
    pathlib.Path(report).unlink()
    assert not pathlib.Path(report).exists()


def test_GenerateModelReport_Failing(sample_without_predictorbinning):
    with pytest.raises(Exception) as e_info:
        sample_without_predictorbinning.generate_model_reports(
            name="MyOrg", model_list="bd70a915-697a-5d43-ab2c-53b0557c85a0"
        )
    assert (
        "model_list argument is None, not a list, or contains non-string elements for generate_model_reports. Please provide a list of model_id strings to generate reports."
        in str(e_info)
    )
