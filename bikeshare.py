import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city=''
    
    while city not in CITY_DATA.keys():
        print("\nWlecome to this program.Please choose your city:")
        print("\n1.Chicago 2.New York City 3.Washington")
        print("\nAccepted input:\nFull Name of city:not case_sensitive.\nFull Name of tile case_sensitive")
        
        city=input().lower()
        if city not in CITY_DATA.keys():
            print("\nPlease check your input")
            print("\nRestarting....")
    print("\nYou have chosen {city.title()} as your city")      
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'all':7}
    month=''
    while month not in MONTH.keys():
        print("\nPlease enter the month,between Jan to Jun:")
        print("\nAccepted input:\nFull month name:not case_sensitive.\nFull month name in title case_sensitive")
        print("\n(You may also choose to view data for all months,type 'all' or 'All' or 'ALL')")
        
        month=input().lower()
        if month not in MONTH.keys():
            print("\nInvalid Input")
            print("\nRestarting")
            
    print("\nYou have chosen {month.title()} as your month")       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY=['all','monday','tuesday','wednesday','thrusday','friday','saturday','sunday']
    day=''
           
    while day not in DAY:
           print("\nPlease enter the day,between mon to sun")
           print("\nAccepted input:\nDay name:not case_sensitive.\nDay name in title case_sensitive")
           print("\n(You may also choose to view data for all days,type 'all' or 'All' or 'ALL')")
           
           day=input().lower()
            
           if day not in DAY:
              print("\nInvalid input")
              print("\Restarting..")
           
    print("\nYou have chosen {day.title()} as your day")
    print("\nYou have chosen to view data for city: {city.upper()},month/s:{month.uppee()} and day/s:{day.upper()}")       
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])                     #Load data
    df['Start Time']=pd.to_datetime(df['Start Time'])   #converting start time col to datetime
    df['month']=df['Start Time'].dt.month                     #extract month from start time
    df['day_of_week']=df['Start Time'].dt.weekday_name        #extract weekday from start time
    df['hour']=df['Start Time'].dt.hour                       #extract hour from start time
    
    if month!='all':                       
        months=['january','february','march','april','may','june']    
        month=months.index(month)+1                     
        
        df=df[df['month']==month]                       #filter by month to create new dataframe
        
    if day!='all':                                      #filter by weekday
        df=df[df['day_of_week']==day.title()]           ##filter by weekday to create new dataframe

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #By using mode() to get the most common set of values of each element along yhe slected axis
    # TO DO: display the most common month
    most_comm_month=df['month'].mode()[0]
    print("Most Common Month (1= January,...,6=June):{}".format(most_comm_month))
    
    # TO DO: display the most common day of week
    most_comm_day=df['day_of_week'].mode()[0]
    print("\nMost Common Day:{}".format(most_comm_day))

    # TO DO: display the most common start hour
    most_comm_hr=df['hour'].mode()[0]
    print("\nMost Common Hour:{}".format(most_comm_hr))                          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_comm_strt_sta=df['Start Station'].mode()[0]
    print("Most Commonly Started Station is:{}".format(most_comm_strt_sta))                          

    # TO DO: display most commonly used end station
    most_comm_end_sta=df['End Station'].mode()[0]
    print("Most Commonly Ended Station is:{}".format(most_comm_end_sta))                          

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End']=df['Start Station']+" "+"to"+" "+df['End Station']
    combined=df['Start To End'].mode()[0]
    print("\nMost frequent combination of trips is:{}".format(combined))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    minu,sec=divmod(total_time,60)
    hr,minu=divmod(minu,60)
    print("Total Trip Duration is:{} hours,{} minutes and {} seconds".format(hr,minu,sec))
    # TO DO: display mean travel time
    avg_duration=round(df['Trip Duration'].mean())
    mi,se=divmod(avg_duration,60)
    if mi>60:
          h,mi=divmod(mi,60)
          print("Total Trip Duration is:{} hours,{} minutes and {} seconds".format(h,mi,se))
    else:
          print("Total Trip Duration is:{} minutes and {} seconds".format(mi,se))
                              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usr_counts=df['User Type'].value_counts()
    print("The User types are:\n",usr_counts)
    # TO DO: Display counts of gender
    if city.title() == 'Chicago' or city.title() =='New york City':
                              gend_cnts=df['Gender'].value_counts()
                              print("\nThe counts of each gender are:\n",gend_cnts)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=int(df['Birth Year'].min())
        print("\nThe oldest user is born of yr",earliest)
                              
        recently=int(df['Birth Year'].max())
        print("\nThe youngest user is born of yr",recently)
                              
        comm=int(df['Birth Year'].mode()[0])
        print("Most users are born of the yr",comm)
    except:
        print("\There are no birth year details")
                              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    BIN_RESPONSE_LIST=['yes','no']
    rdata=''
    c=0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo u wish to view raw data")
        print("\nAccepted respopnse:\nyes or no")
        rdata=input().lower()
                              
        if rdata=="yes":
                  print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:    
                  print("\nPlease check your input")
                  print("Input does not match of accepted response")
                  print("\nRestarting...")
                              
    while rdata=='yes':
        print("Do you wish to view more raw data")
        c+=5
        rdata=input().lower()
                              
        if rdata=="yes":
                 print(df[c:c+5])
        elif rdata!="yes":
                 break             
    print('-'*80)     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
