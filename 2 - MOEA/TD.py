

class TD:
  def __init__(self, _id, _pn, _r_main, _r_d1):
    self.id = _id
    self.pn = _pn
    self.r_main = _r_main
    self.r_d1 = _r_d1
    self.selection = 0

class S:
  def __init__(self, _TDs):
    self.TDs = _TDs

class Cal:  
  Ss = []
  TDs = []

  MaOP = False
  TDs_Full = []
  TDs_Repayment = []
  TDs_Investment = []
  budget = 0.0

  def TDS(self,TD):
    return (TD.r_main*TD.pn)
  def getTotalCost(self):
    return sum(x.pn for x in self.TDs_Full if x.selection != 0)
  def remainBudget(self):
    return self.budget - self.getTotalCost()
  def totalTDS_global(self):
    return sum(self.TDS(x) for x in self.TDs_Repayment)
  def setTDSelection(self, index, selection):
    if(self.MaOP == False):
      ##print("MaOP False")
      ##print("TDs length: "+str(len(self.TDs)))
      ##print(self.TDs)
      self.TDs_Full = self.TDs
    ##else:
      ##print("MaOP True")
    self.MaOP = True
    self.TDs_Full[index].selection = selection
    self.TDs_Repayment = [i for i in self.TDs_Full if i.selection == 1]
    ##print("TDs_Repayment: "+str(len(self.TDs_Repayment)))
    self.TDs = self.TDs_Repayment
  def changeSelectionsSet(self,selectionSets):
    if(self.MaOP == True):
      if(len(selectionSets) == len(self.TDs)):  
        self.MaOP = True
        self.TDs_Full = self.TDs
        for i in range(len(selectionSets)):
          self.TDs_Full[i].selection = selectionSets[i]
        self.TDs_Repayment = [i for i in self.TDs_Full if i.selection == 1]
        self.TDs = self.TDs_Repayment
      else:
        print("Error: No. of selection matrix is not equal to No. of TDs")
        print(str(len(self.TDs))+"::"+str(len(selectionSets)))
    else:
      if(len(selectionSets) == len(self.TDs)):
        self.MaOP = True
        self.TDs_Full = self.TDs
        for i in range(len(selectionSets)):
          self.TDs_Full[i].selection = selectionSets[i]
        self.TDs_Repayment = [i for i in self.TDs_Full if i.selection == 1]
        self.TDs = self.TDs_Repayment
      else:
        print("Error: No. of selection matrix is not equal to No. of TDs")
  def showSelectionSets_global(self):
    for i in self.TDs_Full:
      print(i.selection)
  def getSelectionSets_global(self):
    res = ""
    for i in self.TDs_Full:
      res = res + "," + str(i.selection)
    return res 
  def getSelectionSets_global_array(self):
    res = []
    for i in self.TDs_Full:
      res.append(i.selection)
    return res
  def showSelectionSets_S1(self):
    for i in self.TDs_Full:
      if i in self.Ss[0].TDs:
        print(i.selection)
      else:
        print(0)
  def showSelectionSets_S2(self):
    for i in self.TDs_Full:
      if i in self.Ss[1].TDs:
        print(i.selection)
      else:
        print(0)
  def showSelectionSets_S3(self):
    for i in self.TDs_Full:
      if i in self.Ss[2].TDs:
        print(i.selection)
      else:
        print(0)
  def showInvestmentSelection(self):
    for i in self.TDs_Investment:
      print(i.id)
  def showRepaymentSelection(self):
    for i in self.TDs_Repayment:
      print(i.id)
  def showMember_S1(self):
    for i in self.TDs_Full:
      if i in self.Ss[0].TDs:
        print(i.id)
  def showMember_S2(self):
    for i in self.TDs_Full:
      if i in self.Ss[1].TDs:
        print(i.id)
  def showMember_S3(self):
    for i in self.TDs_Full:
      if i in self.Ss[2].TDs:
        print(i.id)
  def totalTDS_S1(self):
    return sum(self.TDS(x) for x in self.TDs_Repayment if x in self.Ss[0].TDs)
  def totalTDS_S2(self):
    return sum(self.TDS(x) for x in self.TDs_Repayment if x in self.Ss[1].TDs)
  def totalTDS_S3(self):
    return sum(self.TDS(x) for x in self.TDs_Repayment if x in self.Ss[2].TDs)
  def nullSelection(self):
    self.MaOP = True
    for i in range(len(self.TDs_Full)):
      self.TDs_Full[i].selection = 0
    self.TDs_Repayment = [i for i in self.TDs_Full if i.selection == 1]
    self.TDs_Investment = [i for i in self.TDs_Full if i.selection == 2]
    self.TDs = self.TDs_Repayment