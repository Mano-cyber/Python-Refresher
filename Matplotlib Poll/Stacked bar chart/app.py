import matplotlib.pyplot as plt
from data import polls

poll_title = [poll[0] for poll in polls]
poll_men = [poll[1] for poll in polls]
poll_women = [poll[2] for poll in polls]

poll_x_corrdinates = range(len(polls))

figure  = plt.figure(figsize=(6, 6))
figure.subplot_adjust(bottom=0.35)
axes = figure.add_subplot()
axes.bar(
    poll_x_corrdinates,
    poll_men,
)

axes.bar(
    poll_x_corrdinates,
    poll_women,
    bottom=poll_men
)

plt.xticks(poll_x_corrdinates, poll_title, rotation=30, ha="right")

plt.show()