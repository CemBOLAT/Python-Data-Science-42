from datetime import datetime

def format_ft_time():
    current_time = datetime.now()
    print("Seconds since January 1, 1970:", "{:,.4f}".format(current_time.timestamp()), "or", "{:.2e}".format(current_time.timestamp()), "in scientific notation")
    formatted_date = current_time.strftime("%b %d %Y")
    print(formatted_date)

if __name__ == "__main__":
    format_ft_time()


#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$
# call the function in main
