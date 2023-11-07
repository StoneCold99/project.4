def calculate_roi(purchase_price, down_payment, closing_costs, monthly_rent, annual_property_taxes, annual_insurance, annual_maintenance, vacancy_rate, mortgage_term, mortgage_interest_rate):

  """Calculates the return on investment for a rental property.

  Args:
    purchase_price: The purchase price of the property.
    down_payment: The down payment on the property.
    closing_costs: The closing costs associated with the purchase of the property.
    monthly_rent: The monthly rent for the property.
    annual_property_taxes: The annual property taxes for the property.
    annual_insurance: The annual insurance for the property.
    annual_maintenance: The annual maintenance for the property.
    vacancy_rate: The vacancy rate for the property.
    mortgage_term: The term of the mortgage in years.
    mortgage_interest_rate: The interest rate on the mortgage.

  Returns:
    The return on investment for the rental property.
  """

  total_cash_invested = purchase_price - down_payment - closing_costs

  annual_cash_flow = (monthly_rent * 12) - (annual_property_taxes + annual_insurance + annual_maintenance) - (monthly_rent * vacancy_rate)

  monthly_mortgage_payment = (total_cash_invested * mortgage_interest_rate) / (12 * (1 + mortgage_interest_rate)**mortgage_term)

  total_mortgage_payments = monthly_mortgage_payment * (12 * mortgage_term)

  net_cash_flow = annual_cash_flow - total_mortgage_payments

  roi = (net_cash_flow / total_cash_invested) * 100

  return roi

if __name__ == "__main__":

  #  Input from the user.
  purchase_price = float(input("Enter the purchase price of the property: "))
  down_payment = float(input("Enter the down payment on the property: "))
  closing_costs = float(input("Enter the closing costs associated with the purchase of the property: "))
  monthly_rent = float(input("Enter the monthly rent for the property: "))
  annual_property_taxes = float(input("Enter the annual property taxes for the property: "))
  annual_insurance = float(input("Enter the annual insurance for the property: "))
  annual_maintenance = float(input("Enter the annual maintenance for the property: "))
  vacancy_rate = float(input("Enter the vacancy rate for the property: "))
  mortgage_term = int(input("Enter the term of the mortgage in years: "))
  mortgage_interest_rate = float(input("Enter the interest rate on the mortgage: "))

  # Return on investment.
  roi = calculate_roi(purchase_price, down_payment, closing_costs, monthly_rent, annual_property_taxes, annual_insurance, annual_maintenance, vacancy_rate, mortgage_term, mortgage_interest_rate)

  # Print the return on investment.
  print("The return on investment for the rental property is {}%.".format(roi))