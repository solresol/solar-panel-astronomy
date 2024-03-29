import argparse
import datetime

import ephem


def calculate_moon_position_and_phase(date_time, latitude, longitude):
    observer = ephem.Observer()
    observer.date = date_time
    observer.lat = latitude
    observer.lon = longitude
    moon = ephem.Moon(observer)
    return moon.alt, moon.az, moon.phase

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--when', default=datetime.datetime.now(), help='ISO formatted date and time without microseconds')
    parser.add_argument('--latitude', default='-33.7580', help='Observers latitude')
    parser.add_argument('--longitude', default='151.0582', help='Observers longitude')
    args = parser.parse_args()

    alt, az, phase = calculate_moon_position_and_phase(args.when, args.latitude, args.longitude)
    print(f'Moon Position: Altitude = {alt}, Azimuth = {az}')
    print(f'Moon Phase: {phase}')

if __name__ == '__main__':
    main()
