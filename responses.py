import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

participantDF = pd.read_excel(r'C:\Users\maste\University\16. FYP\User Research\Responses Python\SurveryResponses_V2.xlsx', index_col=(0))
n_bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]


participantsExperienced = participantDF[participantDF["Experienced"] == True]
participantsInexperienced = participantDF[~participantDF["Experienced"] == True]

AmmoExp = sum(participantsExperienced["Ammo_Use"])
AmmoInexp = sum(participantsInexperienced["Ammo_Use"])

SWExp = sum(participantsExperienced["SelectedWeapon_Use"])
SWInexp = sum(participantsInexperienced["SelectedWeapon_Use"])

############################################################################
#HUD Element Usefulness between experienced and inexperienced players      #
############################################################################
n_yticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

"""
fig, axs = plt.subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = [1, 2, 3, 4, 5, 6])
fig.suptitle("Crosshair Usefulness")
axs[0].hist(participantsExperienced["Crosshair_Use"], bins=n_bins)
axs[0].set(xlabel='Experienced Participants', ylabel='Frequency')
axs[1].hist(participantsInexperienced["Crosshair_Use"], bins=n_bins, color="orange")
axs[1].set(xlabel='Inexperienced Participants')
plt.show()


fig, axs = plt.subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = [1, 2, 3, 4, 5, 6])
fig.suptitle("Ammo Usefulness")
axs[0].hist(participantsExperienced["Ammo_Use"], bins=n_bins)
axs[0].set(xlabel='Experienced Participants', ylabel='Frequency')
axs[1].hist(participantsInexperienced["Ammo_Use"], bins=n_bins, color="orange")
axs[1].set(xlabel='Inexperienced Participants')
plt.show()


fig, axs = plt.subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = [1, 2, 3, 4, 5, 6])
fig.suptitle("Grenade Usefulness")
axs[0].hist(participantsExperienced["Grenade_Use"], bins=n_bins)
axs[0].set(xlabel='Experienced Participants', ylabel='Frequency')
axs[1].hist(participantsInexperienced["Grenade_Use"], bins=n_bins, color="orange")
axs[1].set(xlabel='Inexperienced Participants')
plt.show()

fig, axs = plt.subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = [1, 2, 3, 4, 5, 6])
fig.suptitle("Selected Weapon Usefulness")
axs[0].hist(participantsExperienced["SelectedWeapon_Use"], bins=n_bins)
axs[0].set(xlabel='Experienced Participants', ylabel='Frequency')
axs[1].hist(participantsInexperienced["SelectedWeapon_Use"], bins=n_bins, color="orange")
axs[1].set(xlabel='Inexperienced Participants')
plt.show()

fig, axs = plt.subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = [1, 2, 3, 4, 5, 6])
fig.suptitle("Vitals Usefulness")
axs[0].hist(participantsExperienced["Vitals_Use"], bins=n_bins)
axs[0].set(xlabel='Experienced Participants', ylabel='Frequency')
axs[1].hist(participantsInexperienced["Vitals_Use"], bins=n_bins, color="orange")
axs[1].set(xlabel='Inexperienced Participants')
plt.show()

fig, axs = plt.subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = [1, 2, 3, 4, 5, 6])
fig.suptitle("Objective Usefulness")
axs[0].hist(participantsExperienced["Objective_Use"], bins=n_bins)
axs[0].set(xlabel='Experienced Participants', ylabel='Frequency')
axs[1].hist(participantsInexperienced["Objective_Use"], bins=n_bins, color="orange")
axs[1].set(xlabel='Inexperienced Participants')
plt.show()
"""
# https://stackoverflow.com/questions/63697432/python-matplotlib-how-to-change-y-values-of-histogram

bigfig = plt.figure(constrained_layout=True, figsize=(15, 10))
fig = bigfig.subfigures(2, 3)

axs = fig[0, 0].subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = n_yticks)
fig[0, 0].suptitle("Crosshair Usefulness", fontsize=20)
axs[0].hist(participantsExperienced["Crosshair_Use"], bins=n_bins)
axs[0].set(ylabel='Frequency')
axs[1].hist(participantsInexperienced["Crosshair_Use"], bins=n_bins, color="orange")
axs[0].set_ylim([0, 10])
axs[1].set_ylim([0, 10])

meanCrosshairExp = participantsExperienced["Crosshair_Use"].describe()
meanCrosshairinExp = participantsInexperienced["Crosshair_Use"].describe()
ttestCrosshair = stats.ttest_ind(participantsInexperienced["Crosshair_Use"], participantsExperienced["Crosshair_Use"])[1]

axs = fig[0, 1].subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = n_yticks)
fig[0, 1].suptitle("Ammo Usefulness", fontsize=20)
axs[0].hist(participantsExperienced["Ammo_Use"], bins=n_bins)
axs[1].hist(participantsInexperienced["Ammo_Use"], bins=n_bins, color="orange")
axs[0].set_ylim([0, 10])
axs[1].set_ylim([0, 10])

meanAmmoExp = participantsExperienced["Ammo_Use"].describe()
meanAmmoinExp = participantsInexperienced["Ammo_Use"].describe()
ttestAmmo = stats.ttest_ind(participantsInexperienced["Ammo_Use"], participantsExperienced["Ammo_Use"])[1]

axs = fig[0, 2].subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = n_yticks)
fig[0, 2].suptitle("Grenade Usefulness", fontsize=20)
axs[0].hist(participantsExperienced["Grenade_Use"], bins=n_bins)
axs[1].hist(participantsInexperienced["Grenade_Use"], bins=n_bins, color="orange")
axs[0].set_ylim([0, 10])
axs[1].set_ylim([0, 10])

meanGrenadeExp = participantsExperienced["Grenade_Use"].describe()
meanGrenadeinExp = participantsInexperienced["Grenade_Use"].describe()
ttestGrenade = stats.ttest_ind(participantsInexperienced["Grenade_Use"], participantsExperienced["Grenade_Use"])[1]

axs = fig[1, 0].subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = n_yticks)
fig[1, 0].suptitle("Selected Weapon Usefulness", fontsize=20)
axs[0].hist(participantsExperienced["SelectedWeapon_Use"], bins=n_bins)
axs[0].set(ylabel='Frequency')
axs[1].hist(participantsInexperienced["SelectedWeapon_Use"], bins=n_bins, color="orange")
axs[0].set_ylim([0, 10])
axs[1].set_ylim([0, 10])

meanSWExp = participantsExperienced["SelectedWeapon_Use"].describe()
meanSWinExp = participantsInexperienced["SelectedWeapon_Use"].describe()
ttestSelectedWeapon = stats.ttest_ind(participantsInexperienced["SelectedWeapon_Use"], participantsExperienced["SelectedWeapon_Use"])[1]

axs = fig[1, 1].subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = n_yticks)
fig[1, 1].suptitle("Vitals Usefulness", fontsize=20)
axs[0].hist(participantsExperienced["Vitals_Use"], bins=n_bins)
axs[1].hist(participantsInexperienced["Vitals_Use"], bins=n_bins, color="orange")
axs[0].set_ylim([0, 10])
axs[1].set_ylim([0, 10])

meanVitalsExp = participantsExperienced["Vitals_Use"].describe()
meanVitalsinExp = participantsInexperienced["Vitals_Use"].describe()
ttestVitals = stats.ttest_ind(participantsInexperienced["Vitals_Use"], participantsExperienced["Vitals_Use"])[1]

axs = fig[1, 2].subplots(1, 2, sharey=True)
plt.setp(axs, xticks=[1, 2, 3, 4, 5, 6], yticks = n_yticks)
fig[1, 2].suptitle("Objective Usefulness", fontsize=20)
axs[0].hist(participantsExperienced["Objective_Use"], bins=n_bins)
axs[1].hist(participantsInexperienced["Objective_Use"], bins=n_bins, color="orange")
axs[0].set_ylim([0, 10])
axs[1].set_ylim([0, 10])
plt.savefig('HUDUsefulnessGraph.png', dpi=400)
plt.show()

meanObjectiveExp = participantsExperienced["Objective_Use"].describe()
meanObjectiveinExp = participantsInexperienced["Objective_Use"].describe()
ttestObjective = stats.ttest_ind(participantsInexperienced["Objective_Use"], participantsExperienced["Objective_Use"])[1]

############################################################################
#HUD Element Position between experienced vs inexperienced players         #
############################################################################
POS_Crosshair_Exp = participantsExperienced.groupby(participantsExperienced["Crosshair_Pos"]).size()
POS_Crosshair_Inexp = participantsInexperienced.groupby(participantsInexperienced["Crosshair_Pos"]).size()

POS_Ammo_Exp = participantsExperienced.groupby(participantsExperienced["Ammo_Pos"]).size()
POS_Ammo_Inexp = participantsInexperienced.groupby(participantsInexperienced["Ammo_Pos"]).size()

POS_Grenade_Exp = participantsExperienced.groupby(participantsExperienced["Grenade_Pos"]).size()
POS_Grenade_Inexp = participantsInexperienced.groupby(participantsInexperienced["Grenade_Pos"]).size()

POS_SelectedWeapon_Exp = participantsExperienced.groupby(participantsExperienced["SelectedWeapon_Pos"]).size()
POS_SelectedWeapon_Inexp = participantsInexperienced.groupby(participantsInexperienced["SelectedWeapon_Pos"]).size()

POS_Vitals_Exp = participantsExperienced.groupby(participantsExperienced["Vitals_Pos"]).size()
POS_Vitals_Inexp = participantsInexperienced.groupby(participantsInexperienced["Vitals_Pos"]).size()

POS_Objective_Exp = participantsExperienced.groupby(participantsExperienced["Objective_Pos"]).size()
POS_Objective_Inexp = participantsInexperienced.groupby(participantsInexperienced["Objective_Pos"]).size()

############################################################################
#Experienced Players                                                     #
############################################################################
# initialize data of lists.
_data_Exp = {#'Crosshair': [POS_Crosshair_Exp["Centre"], 0, 0, 0, 0, 0, 0, POS_Crosshair_Exp["Hidden"]],
             'Ammo': [0, 0, POS_Ammo_Exp["Bottom Centre"], 0, 0, POS_Ammo_Exp["Bottom Left"], POS_Ammo_Exp["Bottom Right"], 0],
             "Grenade": [0, 0, 0, POS_Grenade_Exp["Top Left"], 0, POS_Grenade_Exp["Bottom Left"], POS_Grenade_Exp["Bottom Right"], 0],
             "Selected Weapon": [0, 0, POS_SelectedWeapon_Exp["Bottom Centre"], POS_SelectedWeapon_Exp["Top Left"], 0, POS_SelectedWeapon_Exp["Bottom Left"], POS_SelectedWeapon_Exp["Bottom Right"], POS_SelectedWeapon_Exp["Hidden"]],
             "Vitals": [0, 0, POS_Vitals_Exp["Bottom Centre"], POS_Vitals_Exp["Top Left"], 0, POS_Vitals_Exp["Bottom Left"], POS_Vitals_Exp["Bottom Right"], 0],
             "Objective": [POS_Objective_Exp["Centre"], POS_Objective_Exp["Top Centre"], POS_Objective_Exp["Bottom Centre"], 0, POS_Objective_Exp["Top Right"], POS_Objective_Exp["Bottom Left"], 0, 0]}

# Creates pandas DataFrame.
POS_All_Exp = pd.DataFrame(_data_Exp, index=['Centre',
                                             'Top Centre',
                                             'Bottom Centre',
                                             'Top Left',
                                             "Top Right",
                                             "Bottom Left",
                                             "Bottom Right",
                                             "Hidden"])

std_Ammo_Exp = np.std(POS_All_Exp["Ammo"])
std_Grenade_Exp = np.std(POS_All_Exp["Grenade"])
std_SelectedWeapon_Exp = np.std(POS_All_Exp["Selected Weapon"])
std_Vitals_Exp = np.std(POS_All_Exp["Vitals"])
std_Objective_Exp = np.std(POS_All_Exp["Objective"])

_Centre_Exp = POS_All_Exp.iloc[0]
fig, ax = plt.subplots(3, 3, figsize=(15, 10), sharey=True)
plt.ylim([0, 15])
fig.suptitle("Experienced Players HUD Element Positions", fontsize=20)
ax[1, 1].set_title("Centre", fontsize=20)
_b1 = ax[1, 1].bar(['1', '2', '3', '4', "5"], _Centre_Exp)
_b1[0].set_color('r')
_b1[1].set_color('g')
_b1[2].set_color('b')
_b1[3].set_color('orange')
_b1[4].set_color('purple')
#_b1[5].set_color('orange')

_TopCentre_Exp = POS_All_Exp.iloc[1]
ax[0, 1].set_title("Top Centre", fontsize=20)
_b2 = ax[0, 1].bar(['1', '2', '3', '4', "5"], _TopCentre_Exp)
_b2[0].set_color('r')
_b2[1].set_color('g')
_b2[2].set_color('b')
_b2[3].set_color('orange')
_b2[4].set_color('purple')
#_b2[5].set_color('orange')

_BottomCentre_Exp = POS_All_Exp.iloc[2]
ax[2, 1].set_title("Bottom Centre", fontsize=20)
_b3 = ax[2, 1].bar(['1', '2', '3', '4', "5"], _BottomCentre_Exp)
_b3[0].set_color('r')
_b3[1].set_color('g')
_b3[2].set_color('b')
_b3[3].set_color('orange')
_b3[4].set_color('purple')
#_b3[5].set_color('orange')

_TopLeft_Exp = POS_All_Exp.iloc[3]
ax[0, 0].set_title("Top Left", fontsize=20)
_b4 = ax[0, 0].bar(['1', '2', '3', '4', "5"], _TopLeft_Exp)
_b4[0].set_color('r')
_b4[1].set_color('g')
_b4[2].set_color('b')
_b4[3].set_color('orange')
_b4[4].set_color('purple')
#_b4[5].set_color('orange')

_TopRight_Exp = POS_All_Exp.iloc[4]
ax[0, 2].set_title("Top Right", fontsize=20)
_b5 = ax[0, 2].bar(['1', '2', '3', '4', "5"], _TopRight_Exp)
_b5[0].set_color('r')
_b5[1].set_color('g')
_b5[2].set_color('b')
_b5[3].set_color('orange')
_b5[4].set_color('purple')
#_b5[5].set_color('orange')

_BottomLeft_Exp = POS_All_Exp.iloc[5]
ax[2, 0].set_title("Bottom Left", fontsize=20)
_b6 = ax[2, 0].bar(['1', '2', '3', '4', "5"], _BottomLeft_Exp)
_b6[0].set_color('r')
_b6[1].set_color('g')
_b6[2].set_color('b')
_b6[3].set_color('orange')
_b6[4].set_color('purple')
#_b6[5].set_color('orange')

_BottomRight_Exp = POS_All_Exp.iloc[6]
ax[2, 2].set_title("Bottom Right", fontsize=20)
_b7 = ax[2, 2].bar(['1', '2', '3', '4', "5"], _BottomRight_Exp)
_b7[0].set_color('r')
_b7[1].set_color('g')
_b7[2].set_color('b')
_b7[3].set_color('orange')
_b7[4].set_color('purple')
#_b7[5].set_color('orange')

ax[1, 0].axis('off')
ax[1, 2].axis('off')

ax[0,0].tick_params(axis='x', labelsize=20)
ax[0,1].tick_params(axis='x', labelsize=20)
ax[0,2].tick_params(axis='x', labelsize=20)
ax[1,1].tick_params(axis='x', labelsize=20)
ax[2,0].tick_params(axis='x', labelsize=20)
ax[2,1].tick_params(axis='x', labelsize=20)
ax[2,2].tick_params(axis='x', labelsize=20)

fig.tight_layout()
plt.savefig('HUDPositionGraphExperienced.png', dpi=400)
plt.show()





############################################################################
#Inexperienced Players                                                     #
############################################################################




_data_Inexp = {#'Crosshair': [POS_Crosshair_Inexp["Centre"], 0, 0, 0, 0, 0, 0, 0],
             'Ammo': [POS_Ammo_Inexp["Centre"], 0, 0, POS_Ammo_Inexp["Top Left"], POS_Ammo_Inexp["Top Right"], 0, POS_Ammo_Inexp["Bottom Right"], 0],
             "Grenade": [POS_Grenade_Inexp["Centre"], 0, 0, POS_Grenade_Inexp["Top Left"], POS_Grenade_Inexp["Top Right"], POS_Grenade_Inexp["Bottom Left"], POS_Grenade_Inexp["Bottom Right"], 0],
             "Selected Weapon": [POS_SelectedWeapon_Inexp["Centre"], 0, 0, POS_SelectedWeapon_Inexp["Top Left"], POS_SelectedWeapon_Inexp["Top Right"], POS_SelectedWeapon_Inexp["Bottom Left"], POS_SelectedWeapon_Inexp["Bottom Right"], 0],
             "Vitals": [POS_Vitals_Inexp["Centre"], POS_Vitals_Inexp["Top Centre"], 0, POS_Vitals_Inexp["Top Left"], POS_Vitals_Inexp["Top Right"], 0, 0, 0],
             "Objective": [POS_Objective_Inexp["Centre"], 0, 0, POS_Objective_Inexp["Top Left"], POS_Objective_Inexp["Top Right"], 0, POS_Objective_Inexp["Bottom Right"], 0]}
# Creates pandas DataFrame.
POS_All_inExp = pd.DataFrame(_data_Inexp, index=['Centre',
                                             'Top Centre',
                                             'Bottom Centre',
                                             'Top Left',
                                             "Top Right",
                                             "Bottom Left",
                                             "Bottom Right",
                                             "Hidden"])

_Centre_Exp = POS_All_inExp.iloc[0]
fig, ax = plt.subplots(3, 3, figsize=(15, 10), sharey=True)
fig.suptitle("Inexperienced Players HUD Element Positions", fontsize=20)
ax[1, 1].set_title("Centre", fontsize=20)
_b1 = ax[1, 1].bar(['1', '2', '3', '4', "5"], _Centre_Exp)
_b1[0].set_color('r')
_b1[1].set_color('g')
_b1[2].set_color('b')
_b1[3].set_color('orange')
_b1[4].set_color('purple')
#_b1[5].set_color('orange')



_TopCentre_Exp = POS_All_inExp.iloc[1]
ax[0, 1].set_title("Top Centre", fontsize=20)
_b2 = ax[0, 1].bar(['1', '2', '3', '4', "5"], _TopCentre_Exp)
_b2[0].set_color('r')
_b2[1].set_color('g')
_b2[2].set_color('b')
_b2[3].set_color('orange')
_b2[4].set_color('purple')
#_b2[5].set_color('orange')

_BottomCentre_Exp = POS_All_inExp.iloc[2]
ax[2, 1].set_title("Bottom Centre", fontsize=20)
_b3 = ax[2, 1].bar(['1', '2', '3', '4', "5"], _BottomCentre_Exp)
_b3[0].set_color('r')
_b3[1].set_color('g')
_b3[2].set_color('b')
_b3[3].set_color('orange')
_b3[4].set_color('purple')
#_b3[5].set_color('orange')

_TopLeft_Exp = POS_All_inExp.iloc[3]
ax[0, 0].set_title("Top Left", fontsize=20)
_b4 = ax[0, 0].bar(['1', '2', '3', '4', "5"], _TopLeft_Exp)
_b4[0].set_color('r')
_b4[1].set_color('g')
_b4[2].set_color('b')
_b4[3].set_color('orange')
_b4[4].set_color('purple')
#_b4[5].set_color('orange')

_TopRight_Exp = POS_All_inExp.iloc[4]
ax[0, 2].set_title("Top Right", fontsize=20)
_b5 = ax[0, 2].bar(['1', '2', '3', '4', "5"], _TopRight_Exp)
_b5[0].set_color('r')
_b5[1].set_color('g')
_b5[2].set_color('b')
_b5[3].set_color('orange')
_b5[4].set_color('purple')
#_b5[5].set_color('orange')

_BottomLeft_Exp = POS_All_inExp.iloc[5]
ax[2, 0].set_title("Bottom Left", fontsize=20)
_b6 = ax[2, 0].bar(['1', '2', '3', '4', "5"], _BottomLeft_Exp)
_b6[0].set_color('r')
_b6[1].set_color('g')
_b6[2].set_color('b')
_b6[3].set_color('orange')
_b6[4].set_color('purple')
#_b6[5].set_color('orange')

_BottomRight_Exp = POS_All_inExp.iloc[6]
ax[2, 2].set_title("Bottom Right", fontsize=20)
_b7 = ax[2, 2].bar(['1', '2', '3', '4', "5"], _BottomRight_Exp)
_b7[0].set_color('r')
_b7[1].set_color('g')
_b7[2].set_color('b')
_b7[3].set_color('orange')
_b7[4].set_color('purple')
#_b7[5].set_color('orange')

ax[1, 0].axis('off')
ax[1, 2].axis('off')
plt.ylim([0, 15])

ax[0,0].tick_params(axis='x', labelsize=20)
ax[0,1].tick_params(axis='x', labelsize=20)
ax[0,2].tick_params(axis='x', labelsize=20)
ax[1,1].tick_params(axis='x', labelsize=20)
ax[2,0].tick_params(axis='x', labelsize=20)
ax[2,1].tick_params(axis='x', labelsize=20)
ax[2,2].tick_params(axis='x', labelsize=20)

fig.tight_layout()
plt.savefig('HUDPositionGraphInexperienced.png', dpi=400)
plt.show()


