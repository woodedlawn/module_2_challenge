# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    test_csvpath = Path("./tests/data/output/qualifying_loans.csv")
    test_csvdata = [["Bank of Tests - Test Option","300000","0.85","0.47","740","3.6"]]
    fileio.save_csv(test_csvpath, test_csvdata)

    assert test_csvpath.exists()
    test_csvpath.unlink()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    bank_data_filtered_max_loan_size = max_loan_size.filter_max_loan_size(loan, bank_data)
    for bank in bank_data_filtered_max_loan_size:
        assert int(bank[1]) >= loan

    bank_data_filtered_credit_score = credit_score.filter_credit_score(current_credit_score, bank_data)
    for bank in bank_data_filtered_credit_score:
        assert int(bank[4]) <= current_credit_score
    
    bank_data_filtered_debt_to_income = debt_to_income.filter_debt_to_income(monthly_debt_ratio, bank_data)
    for bank in bank_data_filtered_debt_to_income:
        assert float(bank[3]) >= monthly_debt_ratio
    
    bank_data_filtered_loan_to_value = loan_to_value.filter_loan_to_value(loan_to_value_ratio, bank_data)
    for bank in bank_data_filtered_loan_to_value:
        assert float(bank[2]) >= loan_to_value_ratio

