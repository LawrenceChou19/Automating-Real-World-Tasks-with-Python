#!/usr/bin/env python3

import json
import locale
import sys
import emails
import reports
import os


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
#   locale.setlocale(locale.LC_ALL, 'C') if not working, please try locale -a and change to the values on the resualt
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  car_years = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))  # get the item price
    item_revenue = item["total_sales"] * item_price  # calculate the item revenue
    if item_revenue > max_revenue["revenue"]: # if item revenue is greater than current max revenue
      item["revenue"] = item_revenue  # set the item revenue to the current car's revenue
      max_revenue = item  # set the new max revenue to the current car
    # TODO: also handle max sales / Calculate the car model which had the most sales
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item
    # TODO: also handle most popular car_year
    year = item["car"]["car_year"]
    if year not in car_years:
      car_years[year] = item["total_sales"]
    else:
      car_years[year] += item["total_sales"]

  popular_year_count, popular_year = max(zip(car_years.values(), car_years.keys()))  # get the most popular car year

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales".format(popular_year, popular_year_count)
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  #TODO Sort the data by total sales
  sorted_data = sorted(data, key = lambda i: i['total_sales'], reverse=True)  # sort by total sales, descending
  summary = process_data(data)
  # TODO: turn this into a PDF report
  table_data = cars_dict_to_table(data)
  text_summary = '<br/>\n'.join(summary)
  print(text_summary)
  reports.generate("/tmp/cars.pdf", "A Complete Summary of Monthly Car Sales", text_summary, table_data)
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = '\n'.join(summary)

  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")  # creates email
  emails.send(message)

~
if __name__ == "__main__":
  main(sys.argv)