"""
@author: Sadman Ahmed Shanto
used for creating figures 5,6,7 and 8
"""
import numpy as np
import os
from Obj_Func_Comp import SimInfo
import matplotlib.pyplot as pt 
from matplotlib  import cm


def getABLStatsData(true_a, true_b, Lstring, phiString):
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    returns: a parameters, b parameters, expected Loss eval, index position for true parameters
    """
    csv_folder = 'Param_Sweep/'
    test_folder = 'Test_Set/'
    csv_files = os.listdir(csv_folder)
    sim_info_dict = dict.fromkeys(csv_files)
    for csv_file in csv_files: 
            sim_info_dict[csv_file] = SimInfo(csv_folder=csv_folder,file_name=csv_file)
    a = true_a
    b = true_b
    csv_file_real = 'a-'+str(a)+'b-'+str(b)+'.csv'
    speed_true = np.loadtxt(test_folder+csv_file_real)
    for csv_file in csv_files: 
            sim_info_dict[csv_file].setRealSpeedsData(real_speed_data_new=speed_true)
    L_expectations = dict.fromkeys(csv_files)
    L_dist_vals = dict.fromkeys(csv_files)
    L_plot = [] #tuple of (a, b, expected_L,isRealParam)

    for csv_file in csv_files:
        sim_info =  sim_info_dict[csv_file]
        a_sim = sim_info.a
        b_sim = sim_info.b

        if Lstring == "RMSE":
            L = sim_info.getRMSE
        elif Lstring == "MAE":
            L = sim_info.getMAE
        elif Lstring == "SSE":
            L = sim_info.getSSE
        elif Lstring == "SPD":
            L = sim_info.getSPD
        elif Lstring == "ME":
            L = sim_info.getME
        elif Lstring == "MNE":
            L = sim_info.getMNE
        elif Lstring == "MANE":
            L = sim_info.getMANE
        elif Lstring == "RMSNE":
            L = sim_info.getRMSNE
        elif Lstring == "U":
            L = sim_info.getU

        if phiString == "Mean":
            phi = sim_info.getMean
        elif phiString == "Identity":
            phi = sim_info.getIdentity
        elif phiString == "Amplitude":
            phi = sim_info.getAmplitude
        elif phiString == "Std":
            phi = sim_info.getStD
        elif phiString == "Period":
            phi = sim_info.getPeriod
        elif phiString == "HybridPhi":
            phi = sim_info.getHybridPhi

        L_dist = sim_info.get_L_dist(L,phi) # vector of loss function evals: L(phi(X),phi(y))
        L_expect = sim_info.get_L_Expect(L,phi)
        L_expectations[csv_file] = L_expect
        L_dist_vals[csv_file] = L_dist
        if csv_file == csv_file_real:
            L_plot.append((a_sim, b_sim, L_expect, True))
        else:
            L_plot.append((a_sim, b_sim, L_expect, False))

    a_vals = [i[0] for i in L_plot]
    b_vals = [i[1] for i in L_plot]
    L_vals = [i[2] for i in L_plot]
    TrueIndex = [i[3] for i in L_plot].index(True)
    return a_vals, b_vals, L_vals, TrueIndex


def getLStatsData(true_a, true_b, Lstring, phiString):
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    returns: expected Loss eval, max Loss eval, min Loss eval, index position for true parameters
    """
    csv_folder = 'Param_Sweep/'
    test_folder = 'Test_Set/'
    csv_files = os.listdir(csv_folder)
    # put each siminfo into dict to then later reference
    sim_info_dict = dict.fromkeys(csv_files)
    for csv_file in csv_files: 
            sim_info_dict[csv_file] = SimInfo(csv_folder=csv_folder,file_name=csv_file)
    a = true_a
    b = true_b
    csv_file_real = 'a-'+str(a)+'b-'+str(b)+'.csv'
    speed_true = np.loadtxt(test_folder+csv_file_real)
    for csv_file in csv_files: 
            sim_info_dict[csv_file].setRealSpeedsData(real_speed_data_new=speed_true)
    L_expectations = dict.fromkeys(csv_files)
    L_dist_vals = dict.fromkeys(csv_files)
    L_plot = [] #tuple of (expected, max, min, isRealParam)

    for csv_file in csv_files:
        sim_info =  sim_info_dict[csv_file]

        if Lstring == "RMSE":
            L = sim_info.getRMSE 
        elif Lstring == "MAE":
            L = sim_info.getMAE
        elif Lstring == "SSE":
            L = sim_info.getSSE
        elif Lstring == "SPD":
            L = sim_info.getSPD
        elif Lstring == "ME":
            L = sim_info.getME
        elif Lstring == "MNE":
            L = sim_info.getMNE
        elif Lstring == "MANE":
            L = sim_info.getMANE
        elif Lstring == "RMSNE":
            L = sim_info.getRMSNE
        elif Lstring == "U":
            L = sim_info.getU

        if phiString == "Mean":
            phi = sim_info.getMean
        elif phiString == "Identity":
            phi = sim_info.getIdentity
        elif phiString == "Amplitude":
            phi = sim_info.getAmplitude
        elif phiString == "Std":
            phi = sim_info.getStD
        elif phiString == "Period":
            phi = sim_info.getPeriod
        elif phiString == "HybridPhi":
            phi = sim_info.getHybridPhi

        L_dist = sim_info.get_L_dist(L,phi) # vector of loss function evals: L(phi(X),phi(y))
        L_expect = sim_info.get_L_Expect(L,phi)
        L_expectations[csv_file] = L_expect
        L_dist_vals[csv_file] = L_dist
        if csv_file == csv_file_real:
            L_plot.append((L_expect,max(L_dist),min(L_dist),True))
        else:
            L_plot.append((L_expect,max(L_dist),min(L_dist),False))

    sorted_by_L_exp = sorted(L_plot, key=lambda tup: tup[0])
    x_L_expect = [i for i in range(len(L_plot))]
    L_exp = [i[0] for i in sorted_by_L_exp]
    L_max = [i[1] for i in sorted_by_L_exp]
    L_min = [i[2] for i in sorted_by_L_exp]
    TrueIndex = [i[3] for i in sorted_by_L_exp].index(True)
    return L_exp, L_max, L_min, TrueIndex


def createLossValuesPlot(true_a, true_b, Lstring, phiString):
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    purpose: creates the Loss function statistics plot with true paramet point as red square
    """
    fig = pt.figure()
    L_exp, L_max, L_min, TrueIndex = getLStatsData(true_a, true_b, Lstring, phiString) 
    x_L_expect = [i for i in range(len(L_exp))]
    pt.plot(x_L_expect, L_exp, 'b.', markersize=11)
    pt.plot(x_L_expect, L_max, 'g.', markersize=11)
    pt.plot(x_L_expect, L_min, 'y.', markersize=11)
    #true
    pt.plot(x_L_expect[TrueIndex], L_exp[TrueIndex], 'rs', markersize=10)
    pt.plot(x_L_expect[TrueIndex], L_max[TrueIndex], 'rs', markersize=10)
    pt.plot(x_L_expect[TrueIndex], L_min[TrueIndex], 'rs', markersize=10)
    pt.title("Loss function evaluation comparison: a = {}, b = {}".format(true_a,true_b), fontdict={'size':16})
    pt.xlabel("Loss Function Ranking", fontdict={'size':13})
    pt.ylabel("Loss Function Evaulations", fontdict={'size':13})
    pt.ylim([2.5,8])
    pt.legend(["expected", "max", "min"])
    fig.savefig("figures/a-{}b-{}loss.png".format(true_a,true_b), dpi=600)
    pt.show()
    pt.close(fig)


def createABLCountourPlot(true_a, true_b, Lstring, phiString): 
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    purpose: creates the colored contour plot of tuple (a,b,L expected)
    """
    fig = pt.figure()
    a_vals, b_vals, L_vals, TrueIndex = getABLStatsData(true_a, true_b, Lstring, phiString)
    pt.scatter(a_vals, b_vals, c=L_vals)
    pt.annotate("True Point", (a_vals[TrueIndex], b_vals[TrueIndex]), rotation=60)
    pt.title("a: {}, b: {}".format(true_a, true_b))
    pt.colorbar()
    pt.xlabel("a values")
    pt.ylabel("b values")
    fig.savefig("figures/a-{}b-{}color.png".format(true_a,true_b), dpi=600)
    pt.show()
    pt.close(fig)


def getPercentageLessThanLTrue(true_a, true_b, Lstring, phiString): #horrible name I am sorry
    L_exp, L_max, L_min, TrueIndex = getLStatsData(true_a, true_b, Lstring, phiString) 
    totalPoints = len(L_exp)
    return (TrueIndex*100)/totalPoints


def createAllPossiblePlots(Lstring, phiString):
    """
    call this function to create L statistics and contour colored plots for all true parameter points 
    """
    true_as = [round(0.5+0.1*i,2) for i in range(9)]
    true_bs = [round(1.0+0.1*i,2) for i in range(6)]
    for i in range(len(true_as)):
        for j in range(len(true_bs)):
            createABLCountourPlot(true_as[i],true_bs[j], Lstring, phiString)
            createLossValuesPlot(true_as[i],true_bs[j], Lstring, phiString)


def createPercentageAnalysisColorPlot(LfuncName, PhiFuncName):
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    purpose: creates the contour plot of tuple (a,b,percentage of L exp less than true param)
    """
    fig = pt.figure(figsize=(24,15))
    true_as = [round(0.5+0.1*i,2) for i in range(9)]
    true_bs = [round(1.0+0.1*i,2) for i in range(6)]
    percentages = [] #tuple of (a,b,percentage_val)
    for i in range(len(true_as)):
        for j in range(len(true_bs)):
            percentages.append((true_as[i],true_bs[j],getPercentageLessThanLTrue(true_as[i],true_bs[j], LfuncName, PhiFuncName)))
    a_vals= [i[0] for i in percentages]
    b_vals= [i[1] for i in percentages]
    L_vals= [i[2] for i in percentages]
    x_vals = [i for i in range(len(a_vals))]
    pt.scatter(a_vals, b_vals, c=L_vals, s=100)
#    pt.scatter(a_vals[TrueIndex], b_vals[TrueIndex])
    pt.clim([0,100])
    pt.colorbar()
    score = round(sum(L_vals) /  (len(true_as)*len(true_bs)), 4)
    #pt.title("Loss function: {}, Phi operator: {}, <L,Phi> score = {}".format(LfuncName, PhiFuncName, score))
    pt.title("PPF of {}".format(LfuncName), fontdict={'size':25})
    pt.xlabel("a values",fontdict={'size':20})
    pt.ylabel("b values",fontdict={'size':20})
    fig.savefig("figures/{}and{}color.png".format(LfuncName,PhiFuncName), dpi=600)
    pt.show()
    pt.close(fig)

def getDivergenceOfA(a_real, b_real, Lstring, phiString):
    a_vals, b_vals, L_vals, TrueIndex = getABLStatsData(a_real, b_real, Lstring, phiString)
    L_plot = list(zip(a_vals,L_vals))
    sorted_by_L_exp = sorted(L_plot, key=lambda tup: tup[1])
    a_vals = [i[0] for i in sorted_by_L_exp]
    return abs(a_vals[0] - a_real)

def getDivergenceOfB(a_real, b_real, Lstring, phiString):
    a_vals, b_vals, L_vals, TrueIndex = getABLStatsData(a_real, b_real, Lstring, phiString)
    L_plot = list(zip(b_vals,L_vals))
    sorted_by_L_exp = sorted(L_plot, key=lambda tup: tup[1])
    b_vals = [i[0] for i in sorted_by_L_exp]
    return abs(b_vals[0] - b_real)

def getAverageDivergenceMetrics(LfuncName, PhiFuncName):
    """
    LfuncName = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    PhiFuncName = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    purpose: creates the contour plot of tuple (a,b,percentage of L exp less than true param)
    GG:
        Average Percent Divergence: Across all params the average % of other params with a lower obj. func evaluation
        Average Divergence of a: For all params find the a value that is at the lowest obj func then calculate the abs difference between that and the true a, then a calculate the average of all
        average Divergence of b: same thing but for b
    """
    true_as = [round(0.5+0.1*i,2) for i in range(9)]
    true_bs = [round(1.0+0.1*i,2) for i in range(6)]
    percentages = [] 
    divergences_a = [] 
    divergences_b = [] 
    for i in range(len(true_as)):
        for j in range(len(true_bs)):
            percentages.append((true_as[i],true_bs[j],getPercentageLessThanLTrue(true_as[i],true_bs[j], LfuncName, PhiFuncName)))
            divergences_a.append(getDivergenceOfA(true_as[i],true_bs[j], LfuncName, PhiFuncName)/true_as[i])
            divergences_b.append(getDivergenceOfB(true_as[i],true_bs[j], LfuncName, PhiFuncName)/true_bs[j])
    percentages = [i[2] for i in percentages]
    average_percentage_divergence = sum(percentages) / len(percentages)
    average_divergence_a = 100 * (sum(divergences_a) / len(divergences_a))
    average_divergence_b = 100 * (sum(divergences_b) / len(divergences_b))
    print("L = {}, Phi = {}".format(LfuncName, PhiFuncName))
    print("apd: ", average_percentage_divergence)
    print("ada: ", average_divergence_a)
    print("adb: ", average_divergence_b)
    line = "{},{},apd: {}, apa: {}, apd: {}".format(LfuncName,PhiFuncName,average_percentage_divergence,average_divergence_a,average_divergence_b)
    outF = open("metrics.txt", "a")
    outF.write(line)
    outF.write("\n")
    outF.close()

def getDivergenceABPlots(LfuncName, PhiFuncName):
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    purpose: creates the contour plots of tuples (a,b,percentage div_a), (a,b,percentage div_b)
    """
    true_as = [round(0.5+0.1*i,2) for i in range(9)]
    true_bs = [round(1.0+0.1*i,2) for i in range(6)]
    percentages = [] #tuple of (a,b,div_a,div_b)
    for i in range(len(true_as)):
        for j in range(len(true_bs)):
            div_a = getDivergenceOfA(true_as[i],true_bs[j], LfuncName, PhiFuncName) #* 100
            div_b = getDivergenceOfB(true_as[i],true_bs[j], LfuncName, PhiFuncName) #* 100
            percentages.append((true_as[i], true_bs[j], div_a, div_b))
    a_vals= [i[0] for i in percentages]
    b_vals= [i[1] for i in percentages]
    div_a_vals= [i[2] for i in percentages]
    div_b_vals= [i[3] for i in percentages]
    x_vals = [i for i in range(len(a_vals))]
    plotColorScatterGraph(a_vals, b_vals, div_a_vals, "a", LfuncName, PhiFuncName)
    plotColorScatterGraph(a_vals, b_vals, div_b_vals, "b", LfuncName, PhiFuncName)

def plotColorScatterGraph(a_vals,b_vals,L_vals,typ,LfuncName,PhiFuncName):
    fig = pt.figure(figsize=(24,15))
    pt.scatter(a_vals, b_vals, c=L_vals, s=100)
  #  pt.clim([0,100])
    pt.colorbar()
    pt.title("$PPD_{}$ of {}".format(typ, LfuncName), fontdict={'size':25})
    pt.xlabel("a values",fontdict={'size':20})
    pt.ylabel("b values",fontdict={'size':20})
    fig.savefig("figures/{}and{}anddiv_{}.png".format(LfuncName,PhiFuncName,typ), dpi=600)
   # pt.show()
    pt.close(fig)




def createPercentageAnalysisPlot(LfuncName, PhiFuncName):
    """
    Lstring = string keyword that determines which Loss function to use. Options are {RMSE,SSE,MAE,SPD,}
    phiString = string keyword that determines which phi function to use. Options are {Mean, Identity, Amplitude, Std, Period, HybridPhi}
    purpose: creates the line plot of tuple (a,b,percentage of L exp less than true param)
    """
    fig = pt.figure(figsize=(8.0, 5.0))
    true_as = [round(0.5+0.1*i,2) for i in range(9)]
    true_bs = [round(1.0+0.1*i,2) for i in range(6)]
    percentages = [] #tuple of (a,b,percentage_val)
    for i in range(len(true_as)):
        for j in range(len(true_bs)):
            percentages.append((true_as[i],true_bs[j],getPercentageLessThanLTrue(true_as[i],true_bs[j], LfuncName, PhiFuncName)))
    a_vals= [i[0] for i in percentages]
    b_vals= [i[1] for i in percentages]
    L_vals= [i[2] for i in percentages]
    x_vals = [i for i in range(len(a_vals))]
    params = list(zip(a_vals, b_vals))
    pt.plot(x_vals, L_vals, '-.')
    pt.ylabel("Percentage of points that achieve lower expected loss than true point")
    pt.title("Loss function: {}, Phi operator: {}".format(LfuncName, PhiFuncName))
    pt.ylim([0,100])
    for i, txt in enumerate(params):
        pt.annotate(txt, (x_vals[i], L_vals[i]))
    fig.savefig("figures/{}and{}line.png".format(LfuncName,PhiFuncName), dpi=600)
    pt.show()


def testPlots(Lstring, phiString):
    """
    just to quick test some L and phi functions
    """
    createABLCountourPlot(1.3, 1.2, Lstring, phiString)
    createABLCountourPlot(0.5, 1.2, Lstring, phiString)
    createABLCountourPlot(1.1, 1.5, Lstring, phiString)
    createABLCountourPlot(0.7, 1.0, Lstring, phiString)
    createLossValuesPlot(1.3, 1.2, Lstring, phiString)
    createLossValuesPlot(0.5, 1.2, Lstring, phiString)
    createLossValuesPlot(1.1, 1.5, Lstring, phiString)
    createLossValuesPlot(0.7, 1.0, Lstring, phiString)

def createComparisonTimeSeriesPlot(a_vals, b_vals):
    """
    inputs: 
        a_vals = [a_1, a_2] # two a values
        b_vals = [b_1, b_2] # two corresponding b values
    output: figure 5 (comparison between time series data)
    """
    csv_folder = 'Param_Sweep/'
    csv_files = ["a-"+str(a_vals[0])+"b-"+str(b_vals[0])+".csv","a-"+str(a_vals[1])+"b-"+str(b_vals[1])+".csv"]
    sim_info_dict = dict.fromkeys(csv_files)
    time_series_data = []
    for csv_file in csv_files:
            sim_info_dict[csv_file] = SimInfo(csv_folder=csv_folder,file_name=csv_file)
            time_series_data.append(sim_info_dict[csv_file].speedData)
    xvals = [30*i for i in range(len(time_series_data[0][0]))]
   # print(len(time_series_data[0][9]))

    pt.subplot(1,2,1)
    for i in range(len(time_series_data[0])):
        pt.plot(xvals,time_series_data[0][i],'r')
    pt.title("a = {}, b = {}".format(a_vals[0],b_vals[0]), fontdict={'size':25})
    pt.xlabel("Time [s]", fontdict={'size':20})
    pt.ylabel("Speeds [m/s]", fontdict={'size':20})
    pt.ylim([0,20])
    pt.subplot(1,2,2)
    for i in range(len(time_series_data[1])):
        pt.plot(xvals,time_series_data[1][i],'b')
    pt.title("a = {}, b = {}".format(a_vals[1],b_vals[1]), fontdict={'size':25})
    pt.xlabel("Time [s]", fontdict={'size':20})
    pt.ylabel("Speeds [m/s]", fontdict={'size':20})
    pt.ylim([0,20])
   # pt.savefig("_.png")
    pt.show()


def getAllPlotsAndMetrics(L_funcs, Phi_funcs):
    for l in L_funcs:
        for phi in Phi_funcs:
            getAverageDivergenceMetrics(l, phi)
            getDivergenceABPlots(l,phi)
            #createPercentageAnalysisColorPlot(l, phi)


if __name__ == "__main__":
   # getAverageDivergenceMetrics("SSE", "Identity")
   # createComparisonTimeSeriesPlot([0.5,1.2], [1.3,1.3])
   L_funcs = ["RMSE","ME","SSE","MAE","MANE","MNE","RMSNE","U"]
   Phi_funcs = ["Identity"]
  # createLossValuesPlot(0.5, 1.2, "RMSE", "Identity")
  # Phi_funcs = ["Identity","Mean","Std","Amplitude","Period","HybridPhi"]
   getAllPlotsAndMetrics(L_funcs, Phi_funcs)
