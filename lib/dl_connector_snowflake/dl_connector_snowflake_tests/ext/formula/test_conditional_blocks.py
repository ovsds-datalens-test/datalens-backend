from dl_connector_snowflake_tests.ext.formula.base import SnowFlakeTestBase  # noqa
from dl_formula_testing.testcases.conditional_blocks import DefaultConditionalBlockFormulaConnectorTestSuite


class TestConditionalBlockSnowFlake(SnowFlakeTestBase, DefaultConditionalBlockFormulaConnectorTestSuite):
    pass
