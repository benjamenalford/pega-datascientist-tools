import polars as pl
from IPython.display import display, Markdown
import logging
import sys

logging.disable()


sys.path.append("..")

# from plotly.offline import iplot

# Convenience wrapper functions for quarto, to create nice tables and for plotly charts


def quarto_print(text):

    display(Markdown(text))


def quarto_callout_info(info):
    quarto_print(
        """
::: {.callout-note}
%s
:::
"""
        % info
    )


def quarto_callout_important(info):
    quarto_print(
        """
::: {.callout-important}
%s
:::
"""
        % info
    )


def quarto_callout_no_predictor_data_warning(extra=""):
    quarto_callout_important(f"Predictor Data is not available. {extra}")


def polars_col_exists(df, col):
    return col in df.columns and df.schema[col] != pl.Null
