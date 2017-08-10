# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class financials_2014(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    sap_id = models.CharField(db_column='SAP_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entity_or_parent = models.CharField(max_length=255, blank=True, null=True)
    parent_name = models.CharField(max_length=255, blank=True, null=True)
    currency_of_financials = models.CharField(db_column='Currency_of_Financials', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_financials = models.DateTimeField(db_column='Date_of_Financials', blank=True, null=True)  # Field name made lowercase.
    financial_year = models.IntegerField(db_column='Financial_Year', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=255, blank=True, null=True)  # Field name made lowercase.
    audited = models.CharField(db_column='Audited', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consolidated_unconsolidated = models.CharField(db_column='Consolidated_Unconsolidated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    marketable_securities = models.FloatField(db_column='Marketable_Securities', blank=True, null=True)  # Field name made lowercase.
    accounts_receivable = models.FloatField(db_column='Accounts_Receivable', blank=True, null=True)  # Field name made lowercase.
    inventory = models.FloatField(db_column='Inventory', blank=True, null=True)  # Field name made lowercase.
    accounts_receivable_related_party = models.FloatField(db_column='Accounts_Receivable_Related_Party', blank=True, null=True)  # Field name made lowercase.
    prepayments_accruals = models.FloatField(db_column='Prepayments_Accruals', blank=True, null=True)  # Field name made lowercase.
    other = models.FloatField(db_column='Other', blank=True, null=True)  # Field name made lowercase.
    current_assets = models.FloatField(db_column='Current_Assets', blank=True, null=True)  # Field name made lowercase.
    net_ppe_fixed_assets = models.FloatField(db_column='Net_PPE_Fixed_Assets', blank=True, null=True)  # Field name made lowercase.
    prepaid_expenses_greater_1_year = models.FloatField(db_column='Prepaid_Expenses_greater_1_year', blank=True, null=True)  # Field name made lowercase.
    long_term_investments = models.FloatField(db_column='Long_term_Investments', blank=True, null=True)  # Field name made lowercase.
    related_party_investment = models.FloatField(db_column='Related_Party_Investment', blank=True, null=True)  # Field name made lowercase.
    other_assets = models.FloatField(db_column='Other_Assets', blank=True, null=True)  # Field name made lowercase.
    intangible_assets = models.FloatField(db_column='Intangible_Assets', blank=True, null=True)  # Field name made lowercase.
    total_long_term_assets = models.FloatField(db_column='Total_Long_Term_Assets', blank=True, null=True)  # Field name made lowercase.
    total_assets = models.FloatField(db_column='Total_Assets', blank=True, null=True)  # Field name made lowercase.
    short_term_borrowings = models.FloatField(db_column='Short_Term_Borrowings', blank=True, null=True)  # Field name made lowercase.
    accounts_payable_trade = models.FloatField(db_column='Accounts_Payable_Trade', blank=True, null=True)  # Field name made lowercase.
    accounts_payable_related_party = models.FloatField(db_column='Accounts_Payable_Related_Party', blank=True, null=True)  # Field name made lowercase.
    accrued_expenses = models.FloatField(db_column='Accrued_Expenses', blank=True, null=True)  # Field name made lowercase.
    current_portion_of_lt_debt = models.FloatField(db_column='Current_Portion_of_LT_Debt', blank=True, null=True)  # Field name made lowercase.
    other_current_liabilities = models.FloatField(db_column='Other_Current_Liabilities', blank=True, null=True)  # Field name made lowercase.
    current_liabilities = models.FloatField(db_column='Current_Liabilities', blank=True, null=True)  # Field name made lowercase.
    long_term_debt_bank = models.FloatField(db_column='Long_term_Debt_Bank', blank=True, null=True)  # Field name made lowercase.
    related_party_liability = models.FloatField(db_column='Related_Party_Liability', blank=True, null=True)  # Field name made lowercase.
    other_non_current_liabilities = models.FloatField(db_column='Other_Non_Current_Liabilities', blank=True, null=True)  # Field name made lowercase.
    long_term_liabilities = models.FloatField(db_column='Long_Term_Liabilities', blank=True, null=True)  # Field name made lowercase.
    total_liabilities = models.FloatField(db_column='Total_Liabilities', blank=True, null=True)  # Field name made lowercase.
    common_stock = models.FloatField(db_column='Common_Stock', blank=True, null=True)  # Field name made lowercase.
    called_up_share_capital = models.FloatField(db_column='Called_Up_Share_Capital', blank=True, null=True)  # Field name made lowercase.
    preferred_stock = models.FloatField(db_column='Preferred_Stock', blank=True, null=True)  # Field name made lowercase.
    retained_earnings = models.FloatField(db_column='Retained_Earnings', blank=True, null=True)  # Field name made lowercase.
    reserves = models.FloatField(db_column='Reserves', blank=True, null=True)  # Field name made lowercase.
    other_equity = models.FloatField(db_column='Other_Equity', blank=True, null=True)  # Field name made lowercase.
    shareholders_equity = models.FloatField(db_column='Shareholders_Equity', blank=True, null=True)  # Field name made lowercase.
    total_liability_equity = models.FloatField(db_column='Total_Liability_Equity', blank=True, null=True)  # Field name made lowercase.
    sales = models.FloatField(db_column='Sales', blank=True, null=True)  # Field name made lowercase.
    cost_of_goods_sold = models.FloatField(db_column='Cost_of_Goods_Sold', blank=True, null=True)  # Field name made lowercase.
    gross_profit = models.FloatField(db_column='Gross_Profit', blank=True, null=True)  # Field name made lowercase.
    selling_expenses = models.FloatField(db_column='Selling_Expenses', blank=True, null=True)  # Field name made lowercase.
    general_expenses = models.FloatField(db_column='General_Expenses', blank=True, null=True)  # Field name made lowercase.
    depreciation = models.FloatField(db_column='Depreciation', blank=True, null=True)  # Field name made lowercase.
    restructuring_expenses = models.FloatField(db_column='Restructuring_Expenses', blank=True, null=True)  # Field name made lowercase.
    gain_or_loss_goodwill_impairment = models.FloatField(db_column='Gain_or_Loss_Goodwill_impairment', blank=True, null=True)  # Field name made lowercase.
    non_recurring_items = models.FloatField(db_column='Non_Recurring_Items', blank=True, null=True)  # Field name made lowercase.
    operating_expense = models.FloatField(db_column='Operating_Expense', blank=True, null=True)  # Field name made lowercase.
    operating_income = models.FloatField(db_column='Operating_Income', blank=True, null=True)  # Field name made lowercase.
    interest_income = models.FloatField(db_column='Interest_Income', blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(db_column='Other_Income', blank=True, null=True)  # Field name made lowercase.
    interest_expense = models.FloatField(db_column='Interest_Expense', blank=True, null=True)  # Field name made lowercase.
    other_expense = models.FloatField(db_column='Other_Expense', blank=True, null=True)  # Field name made lowercase.
    extradordinary_items = models.FloatField(db_column='Extradordinary_Items', blank=True, null=True)  # Field name made lowercase.
    net_profit_before_taxes = models.FloatField(db_column='Net_Profit_Before_Taxes', blank=True, null=True)  # Field name made lowercase.
    income_taxes = models.FloatField(db_column='Income_Taxes', blank=True, null=True)  # Field name made lowercase.
    net_profit_after_taxes = models.FloatField(db_column='Net_Profit_After_Taxes', blank=True, null=True)  # Field name made lowercase.
    dividends = models.FloatField(db_column='Dividends', blank=True, null=True)  # Field name made lowercase.
    minority_interests = models.FloatField(db_column='Minority_Interests', blank=True, null=True)  # Field name made lowercase.
    commentary = models.CharField(db_column='Commentary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quarter_numb = models.FloatField(db_column='Quarter_numb', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'financials_2014'


class financials_2015(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False,primary_key=True)  # Field name made lowercase.
    sap_id = models.CharField(db_column='SAP_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entity_or_parent = models.CharField(max_length=255, blank=True, null=True)
    parent_name = models.CharField(max_length=255, blank=True, null=True)
    currency_of_financials = models.CharField(db_column='Currency_of_Financials', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_financials = models.DateTimeField(db_column='Date_of_Financials', blank=True, null=True)  # Field name made lowercase.
    financial_year = models.IntegerField(db_column='Financial_Year', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=255, blank=True, null=True)  # Field name made lowercase.
    audited = models.CharField(db_column='Audited', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consolidated_unconsolidated = models.CharField(db_column='Consolidated_Unconsolidated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    marketable_securities = models.FloatField(db_column='Marketable_Securities', blank=True, null=True)  # Field name made lowercase.
    accounts_receivable = models.FloatField(db_column='Accounts_Receivable', blank=True, null=True)  # Field name made lowercase.
    inventory = models.FloatField(db_column='Inventory', blank=True, null=True)  # Field name made lowercase.
    accounts_receivable_related_party = models.FloatField(db_column='Accounts_Receivable_Related_Party', blank=True, null=True)  # Field name made lowercase.
    prepayments_accruals = models.FloatField(db_column='Prepayments_Accruals', blank=True, null=True)  # Field name made lowercase.
    other = models.FloatField(db_column='Other', blank=True, null=True)  # Field name made lowercase.
    current_assets = models.FloatField(db_column='Current_Assets', blank=True, null=True)  # Field name made lowercase.
    net_ppe_fixed_assets = models.FloatField(db_column='Net_PPE_Fixed_Assets', blank=True, null=True)  # Field name made lowercase.
    prepaid_expenses_greater_1_year = models.FloatField(db_column='Prepaid_Expenses_greater_1_year', blank=True, null=True)  # Field name made lowercase.
    long_term_investments = models.FloatField(db_column='Long_term_Investments', blank=True, null=True)  # Field name made lowercase.
    related_party_investment = models.FloatField(db_column='Related_Party_Investment', blank=True, null=True)  # Field name made lowercase.
    other_assets = models.FloatField(db_column='Other_Assets', blank=True, null=True)  # Field name made lowercase.
    intangible_assets = models.FloatField(db_column='Intangible_Assets', blank=True, null=True)  # Field name made lowercase.
    total_long_term_assets = models.FloatField(db_column='Total_Long_Term_Assets', blank=True, null=True)  # Field name made lowercase.
    total_assets = models.FloatField(db_column='Total_Assets', blank=True, null=True)  # Field name made lowercase.
    short_term_borrowings = models.FloatField(db_column='Short_Term_Borrowings', blank=True, null=True)  # Field name made lowercase.
    accounts_payable_trade = models.FloatField(db_column='Accounts_Payable_Trade', blank=True, null=True)  # Field name made lowercase.
    accounts_payable_related_party = models.FloatField(db_column='Accounts_Payable_Related_Party', blank=True, null=True)  # Field name made lowercase.
    accrued_expenses = models.FloatField(db_column='Accrued_Expenses', blank=True, null=True)  # Field name made lowercase.
    current_portion_of_lt_debt = models.FloatField(db_column='Current_Portion_of_LT_Debt', blank=True, null=True)  # Field name made lowercase.
    other_current_liabilities = models.FloatField(db_column='Other_Current_Liabilities', blank=True, null=True)  # Field name made lowercase.
    current_liabilities = models.FloatField(db_column='Current_Liabilities', blank=True, null=True)  # Field name made lowercase.
    long_term_debt_bank = models.FloatField(db_column='Long_term_Debt_Bank', blank=True, null=True)  # Field name made lowercase.
    related_party_liability = models.FloatField(db_column='Related_Party_Liability', blank=True, null=True)  # Field name made lowercase.
    other_non_current_liabilities = models.FloatField(db_column='Other_Non_Current_Liabilities', blank=True, null=True)  # Field name made lowercase.
    long_term_liabilities = models.FloatField(db_column='Long_Term_Liabilities', blank=True, null=True)  # Field name made lowercase.
    total_liabilities = models.FloatField(db_column='Total_Liabilities', blank=True, null=True)  # Field name made lowercase.
    common_stock = models.FloatField(db_column='Common_Stock', blank=True, null=True)  # Field name made lowercase.
    called_up_share_capital = models.FloatField(db_column='Called_Up_Share_Capital', blank=True, null=True)  # Field name made lowercase.
    preferred_stock = models.FloatField(db_column='Preferred_Stock', blank=True, null=True)  # Field name made lowercase.
    retained_earnings = models.FloatField(db_column='Retained_Earnings', blank=True, null=True)  # Field name made lowercase.
    reserves = models.FloatField(db_column='Reserves', blank=True, null=True)  # Field name made lowercase.
    other_equity = models.FloatField(db_column='Other_Equity', blank=True, null=True)  # Field name made lowercase.
    shareholders_equity = models.FloatField(db_column='Shareholders_Equity', blank=True, null=True)  # Field name made lowercase.
    total_liability_equity = models.FloatField(db_column='Total_Liability_Equity', blank=True, null=True)  # Field name made lowercase.
    sales = models.FloatField(db_column='Sales', blank=True, null=True)  # Field name made lowercase.
    cost_of_goods_sold = models.FloatField(db_column='Cost_of_Goods_Sold', blank=True, null=True)  # Field name made lowercase.
    gross_profit = models.FloatField(db_column='Gross_Profit', blank=True, null=True)  # Field name made lowercase.
    selling_expenses = models.FloatField(db_column='Selling_Expenses', blank=True, null=True)  # Field name made lowercase.
    general_expenses = models.FloatField(db_column='General_Expenses', blank=True, null=True)  # Field name made lowercase.
    depreciation = models.FloatField(db_column='Depreciation', blank=True, null=True)  # Field name made lowercase.
    restructuring_expenses = models.FloatField(db_column='Restructuring_Expenses', blank=True, null=True)  # Field name made lowercase.
    gain_or_loss_goodwill_impairment = models.FloatField(db_column='Gain_or_Loss_Goodwill_impairment', blank=True, null=True)  # Field name made lowercase.
    non_recurring_items = models.FloatField(db_column='Non_Recurring_Items', blank=True, null=True)  # Field name made lowercase.
    operating_expense = models.FloatField(db_column='Operating_Expense', blank=True, null=True)  # Field name made lowercase.
    operating_income = models.FloatField(db_column='Operating_Income', blank=True, null=True)  # Field name made lowercase.
    interest_income = models.FloatField(db_column='Interest_Income', blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(db_column='Other_Income', blank=True, null=True)  # Field name made lowercase.
    interest_expense = models.FloatField(db_column='Interest_Expense', blank=True, null=True)  # Field name made lowercase.
    other_expense = models.FloatField(db_column='Other_Expense', blank=True, null=True)  # Field name made lowercase.
    extradordinary_items = models.FloatField(db_column='Extradordinary_Items', blank=True, null=True)  # Field name made lowercase.
    net_profit_before_taxes = models.FloatField(db_column='Net_Profit_Before_Taxes', blank=True, null=True)  # Field name made lowercase.
    income_taxes = models.FloatField(db_column='Income_Taxes', blank=True, null=True)  # Field name made lowercase.
    net_profit_after_taxes = models.FloatField(db_column='Net_Profit_After_Taxes', blank=True, null=True)  # Field name made lowercase.
    dividends = models.FloatField(db_column='Dividends', blank=True, null=True)  # Field name made lowercase.
    minority_interests = models.FloatField(db_column='Minority_Interests', blank=True, null=True)  # Field name made lowercase.
    commentary = models.CharField(db_column='Commentary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quarter_numb = models.FloatField(db_column='Quarter_numb', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'financials_2015'


class partner_gen_info(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False,primary_key=True)  # Field name made lowercase.
    sap_id = models.CharField(db_column='SAP_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country_of_incorporation = models.CharField(db_column='Country_of_Incorporation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    business_line = models.CharField(db_column='Business_Line', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year_of_incorporation_yyyy = models.CharField(db_column='Year_of_Incorporation_YYYY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    legal_status = models.CharField(db_column='Legal_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=255, blank=True, null=True)  # Field name made lowercase.
    principal_activities_industry = models.CharField(db_column='Principal_activities_industry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_employees = models.CharField(db_column='Number_of_employees', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_registration_number = models.CharField(db_column='Company_Registration_number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vat_number = models.CharField(db_column='VAT_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_vat_number_valid = models.CharField(db_column='Is_VAT_Number_Valid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name_of_the_parent = models.CharField(db_column='Name_of_the_Parent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name_of_ultimate_parent_company = models.CharField(db_column='Name_of_Ultimate_Parent_Company', max_length=255, blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country_of_group_incorporation = models.CharField(db_column='Country_of_Group_Incorporation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    percentage_owned_by_group = models.CharField(db_column='Percentage_owned_by_Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wwcs_region = models.CharField(db_column='WWCS_Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_status = models.CharField(db_column='Customer_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shared_financials = models.CharField(db_column='Shared_Financials', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_email_1 = models.CharField(db_column='Customer_email_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_email_2 = models.CharField(db_column='Customer_email_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_email_3 = models.CharField(db_column='Customer_email_3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pam_email_1 = models.CharField(db_column='PAM_email_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pam_email_2 = models.CharField(db_column='PAM_email_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pam_email_3 = models.CharField(db_column='PAM_email_3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_last_updated_date = models.DateTimeField(blank=True, null=True)
    email_last_updated_by = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'partner_gen_info'


class payment_performance(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    sap_id = models.CharField(db_column='SAP_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    revenue_roll_usd_12_months = models.IntegerField(db_column='Revenue_Roll_USD_12_months', blank=True, null=True)  # Field name made lowercase.
    total_usd = models.IntegerField(db_column='Total_USD', blank=True, null=True)  # Field name made lowercase.
    current_usd = models.IntegerField(db_column='Current_USD', blank=True, null=True)  # Field name made lowercase.
    overdue_31_60 = models.IntegerField(db_column='Overdue_31_60', blank=True, null=True)  # Field name made lowercase.
    overdue_1_31 = models.IntegerField(db_column='Overdue_1_31', blank=True, null=True)  # Field name made lowercase.
    overdue = models.IntegerField(db_column='Overdue', blank=True, null=True)  # Field name made lowercase.
    overdue_60_plus = models.IntegerField(db_column='Overdue_60_plus', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'payment_performance'
