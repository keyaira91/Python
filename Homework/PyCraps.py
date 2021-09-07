import requests

games = int(input("How many trails to run: "))
url = f"https://pycraps.herokuapp.com/api/stats/{games}"
r = requests.get(url)
gamedata = r.json()
print(f"Status code: {r.status_code}")
results = gamedata['results']
# print(results)

rolls = [roll['rolls'] for roll in results]
loss = [lose['losses'] for lose in results]
win = [wins['wins'] for wins in results]
win_percent = [(winp['wins'] / games) for winp in results]
game_total = [(game['losses'] + game['wins']) for game in results]
loss_sum = sum(loss)
win_sum = sum(win)
winp_sum = sum(win_percent)

for i in range(len(results)):
    print(f'Roll:\t {rolls[i]},\t Games:\t{game_total[i]},\t Losses:\t{loss[i]},\t Wins:\t {win[i]},\t Win%:\t {win_percent[i]:.0%}')
print(f'TOTAL:\t\t Games: {games},\t Losses: \t{loss_sum},\t Wins: \t {win_sum} ,\t Win%: \t {winp_sum:.0%}')

