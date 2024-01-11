from nba_api.stats.endpoints import LeagueLeaders

def userInput():
    season = input("What NBA season would you like to view? ex: (2022-23): ")
    mode = input("What mode would you like to view? (Totals, Per48, PerGame): ")
    return season, mode

def getTop10Players(leagueLeaders, selected_stat):
    # Sort by the selected stat
    sortedData = leagueLeaders[selectStats].sort_values(by=selected_stat, ascending=False).reset_index(drop=True)

    # Ranks the players based off the user's stat input
    sortedData['RANK'] = sortedData[selected_stat].rank(ascending=False, method='min')

    top10Players = sortedData.head(10)
    return top10Players

if __name__ == "__main__":
    while True:
        season, mode = userInput()

        leagueLeaders = LeagueLeaders(
            league_id='00',  # NBA: '00', G-League: '20', WNBA: '10'
            season=f'{season}',  # Change the year(s) if needed
            per_mode48=f'{mode}',  # "Totals", "Per48", "PerGame"
        )

        # Get data from the year
        leagueLeaders = leagueLeaders.get_data_frames()[0]

        # Select specific columns
        selectStats = ['RANK', 'PLAYER', 'TEAM', 'GP', 'PTS', 'AST', 'OREB', 'DREB', 'STL', 'BLK', 'EFF', 'MIN', 'FGM', 'FGA', 'FTA']

        # Display stats
        print("\nSelect a stat to sort by:")
        for i, stat in enumerate(selectStats[3:]):  # Start at index 3 to skip RANK, PLAYER, TEAM
            print(f"{i+1}. {stat}")

        userChoice = int(input("Enter the number of the stat to sort by (1-13): ")) + 2

        if 3 <= userChoice < len(selectStats):
            selectedStat = selectStats[userChoice]
            print(f"\nSorting by {selectedStat}:\n")

            top10Players = getTop10Players(leagueLeaders, selectedStat)
            print(top10Players)
        else:
            print("Invalid choice. Please enter a number between 1 and 13.")

        runAgain = input("Do you want to view another set of statistics? (Y/N): ")
        if runAgain.lower() != 'y':
            break
