"""saitama"""
def main():
    """saitama"""
    pushup_target = int(input())
    situp_target = int(input())
    crunch_target = int(input())
    run_target = int(input())


    pushup_per_day = int(input())
    situp_per_day = int(input())
    run_per_day = int(input())
    crunch_per_day = int(input())


    days_pushup = (pushup_target + pushup_per_day - 1) // pushup_per_day
    days_situp = (situp_target + situp_per_day - 1) // situp_per_day
    days_crunch = (crunch_target + crunch_per_day - 1) // crunch_per_day
    days_run = (run_target + run_per_day - 1) // run_per_day


    print(max(days_pushup, days_situp, days_crunch, days_run))
main()
