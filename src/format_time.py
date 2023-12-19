
class TimeConversion:
    def cooking_time_formatted (time):
        # Convert float result to Time Format
        hours, minutes = divmod(int(time * 60), 60)
        format_time = f"{hours}:{minutes:02d}"
        timeFormatted = str(format_time)
        print(f"Time Formatted: {timeFormatted}")
        return timeFormatted