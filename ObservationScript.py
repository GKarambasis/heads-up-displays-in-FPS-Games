import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'C:\Users\maste\University\16. FYP\GameUITable.xlsx', index_col=(0))


POS_Vitals_Games = df.groupby(df["Vitals_Pos"]).size()
VPos = (15/(15+3+4+4+6+1))*100
dfVitalDesign = df.groupby(df["Vitals_Design"]).size()
VDesign = (21/(21+11+1))*100

POS_Minimap_Games = df.groupby(df["Minimap_Pos"]).size()
MMPos = (16/(16+7+2))*100
dfMinimapDesign = df.groupby(df["Minimap_Design"]).size()
MMDesign = (15/(15+10))*100

POS_Ammo_Games = df.groupby(df["Ammo_Pos"]).size()
AMPos = (29/(2+2+29+2+5))*100
dfAmmoDesign = df.groupby(df["Ammo_Design"]).size()
AMDesign = (25/40)*100

POS_Grenade_Games = df.groupby(df["Throwables_Position"]).size()
ThrowPos = (23/(23+6+3+2+1))*100

POS_Objective_Games = df.groupby(df["CurrentObjective_Pos"]).size()
CurrentObjectivePos = (8/(8+6+4+3+1))*100

POS_SelectedWeapon_Games = df.groupby(df["Selected_Weapon_Pos"]).size()
SWPos = (17/(17+5+4+2+1))*100

#VPos
#VDesign

dfdescrib = df.describe()

elementDF = {"Vitals": (df.groupby(df["Vitals"]).size()[True]/df.shape[0])*100,
             "Minimap": (df.groupby(df["Minimap"]).size()[True]/df.shape[0])*100,
             "Ammo": (df.groupby(df["Ammo"]).size()[True]/df.shape[0])*100,
             "Compass": (df.groupby(df["Compass"]).size()[True]/df.shape[0])*100,
             "Crosshair": (df.groupby(df["Crosshair"]).size()[True]/df.shape[0])*100,
             "Score": (df.groupby(df["Score"]).size()[True]/df.shape[0])*100,
             "Damage Numbers": (df.groupby(df["DamageNumber"]).size()[True]/df.shape[0])*100,
             "Hitmarker": (df.groupby(df["Hitmarker"]).size()[True]/df.shape[0])*100,
             "Throwables": (df.groupby(df["Throwables"]).size()[True]/df.shape[0])*100,
             "Objective Marker": (df.groupby(df["ObjectiveMarker"]).size()[True]/df.shape[0])*100,
             "Selected Weapon": (df.groupby(df["Selected_Weapon"]).size()[True]/df.shape[0])*100,
             "Current Objective": (df.groupby(df["CurrentObjective"]).size()[True]/df.shape[0])*100}


############################################################################
#Games                                                                     #
############################################################################

_data_Games = {#'Crosshair': [37, 0, 0, 0, 0, 0, 0, 0],
             'Ammo': [0, 0, POS_Ammo_Games["Bottom Centre"], POS_Ammo_Games["Top Left"], POS_Ammo_Games["Top Right"], POS_Ammo_Games["Bottom Left"], POS_Ammo_Games["Bottom Right"], 0],
             "Grenade": [0, 0, POS_Grenade_Games["Bottom Centre"], POS_Grenade_Games["Top Left"], 0, POS_Grenade_Games["Bottom Left"], POS_Grenade_Games["Bottom Right"], 0],
             "Selected Weapon": [0, 0, POS_SelectedWeapon_Games["Bottom Centre"], POS_SelectedWeapon_Games["Top Left"], POS_SelectedWeapon_Games["Top Right"], POS_SelectedWeapon_Games["Bottom Left"], POS_SelectedWeapon_Games["Bottom Right"], 0],
             "Vitals": [0, POS_Vitals_Games["Top Centre"], POS_Vitals_Games["Bottom Centre"], POS_Vitals_Games["Top Left"], POS_Vitals_Games["Top Right"], POS_Vitals_Games["Bottom Left"], POS_Vitals_Games["Bottom Right"], 0],
             "Objective": [0, POS_Objective_Games["Top Centre"], POS_Objective_Games["Bottom Centre"], POS_Objective_Games["Top Left"], POS_Objective_Games["Top Right"], POS_Objective_Games["Bottom Left"], 0, 0]}

# Creates pandas DataFrame.
POS_All_Games = pd.DataFrame(_data_Games, index=['Centre',
                                             'Top Centre',
                                             'Bottom Centre',
                                             'Top Left',
                                             "Top Right",
                                             "Bottom Left",
                                             "Bottom Right",
                                             "Hidden"])

std_Ammo_Games = np.std(POS_All_Games["Ammo"])
std_Grenade_Games = np.std(POS_All_Games["Grenade"])
std_SelectedWeapon_Games = np.std(POS_All_Games["Selected Weapon"])
std_Vitals_Games = np.std(POS_All_Games["Vitals"])
std_Objective_Games = np.std(POS_All_Games["Objective"])

_Centre_Exp = POS_All_Games.iloc[0]
fig, ax = plt.subplots(3, 3, figsize=(15, 10), sharey=True)
fig.suptitle("AAA Games HUD Element Positions", fontsize=20)
ax[1, 1].set_title("Centre", fontsize=20)
_b1 = ax[1, 1].bar(['1', '2', '3', '4', "5"], _Centre_Exp)
_b1[0].set_color('r')
_b1[1].set_color('g')
_b1[2].set_color('b')
_b1[3].set_color('orange')
_b1[4].set_color('purple')
#_b1[5].set_color('orange')

_TopCentre_Exp = POS_All_Games.iloc[1]
ax[0, 1].set_title("Top Centre", fontsize=20)
_b2 = ax[0, 1].bar(['1', '2', '3', '4', "5"], _TopCentre_Exp)
_b2[0].set_color('r')
_b2[1].set_color('g')
_b2[2].set_color('b')
_b2[3].set_color('orange')
_b2[4].set_color('purple')
#_b2[5].set_color('orange')

_BottomCentre_Exp = POS_All_Games.iloc[2]
ax[2, 1].set_title("Bottom Centre", fontsize=20)
_b3 = ax[2, 1].bar(['1', '2', '3', '4', "5"], _BottomCentre_Exp)
_b3[0].set_color('r')
_b3[1].set_color('g')
_b3[2].set_color('b')
_b3[3].set_color('orange')
_b3[4].set_color('purple')
#_b3[5].set_color('orange')

_TopLeft_Exp = POS_All_Games.iloc[3]
ax[0, 0].set_title("Top Left", fontsize=20)
_b4 = ax[0, 0].bar(['1', '2', '3', '4', "5"], _TopLeft_Exp)
_b4[0].set_color('r')
_b4[1].set_color('g')
_b4[2].set_color('b')
_b4[3].set_color('orange')
_b4[4].set_color('purple')
#_b4[5].set_color('orange')

_TopRight_Exp = POS_All_Games.iloc[4]
ax[0, 2].set_title("Top Right", fontsize=20)
_b5 = ax[0, 2].bar(['1', '2', '3', '4', "5"], _TopRight_Exp)
_b5[0].set_color('r')
_b5[1].set_color('g')
_b5[2].set_color('b')
_b5[3].set_color('orange')
_b5[4].set_color('purple')
#_b5[5].set_color('orange')

_BottomLeft_Exp = POS_All_Games.iloc[5]
ax[2, 0].set_title("Bottom Left", fontsize=20)
_b6 = ax[2, 0].bar(['1', '2', '3', '4', "5"], _BottomLeft_Exp)
_b6[0].set_color('r')
_b6[1].set_color('g')
_b6[2].set_color('b')
_b6[3].set_color('orange')
_b6[4].set_color('purple')
#_b6[5].set_color('orange')


_BottomRight_Exp = POS_All_Games.iloc[6]
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
plt.ylim([0, 40])

ax[0,0].tick_params(axis='x', labelsize=20)
ax[0,1].tick_params(axis='x', labelsize=20)
ax[0,2].tick_params(axis='x', labelsize=20)
ax[1,1].tick_params(axis='x', labelsize=20)
ax[2,0].tick_params(axis='x', labelsize=20)
ax[2,1].tick_params(axis='x', labelsize=20)
ax[2,2].tick_params(axis='x', labelsize=20)

fig.tight_layout()
plt.savefig('HUDPositionGraphGames.png', dpi=400)
plt.show()
