def perform(country):
  gl_list=[]
  for i in range(units_len):
    init_machines=0
    n=0
    while init_machines != 1:
      if not countries[country][units_len-1-i] or capacity < units[units_len-1-i]:
        break
      tu=capacity
      sub_list=[]
      index=0
      for j in range(units_len-1-i,-1,-1):
        if countries[country][j]:
          if units[j] <= tu:
            if index == 0:
              init_machines=(tu//units[j])-n
              no_machines=init_machines
            else:
              no_machines=tu//units[j]
            remaining = tu - (no_machines*units[j])
            tu=remaining
            sub_list.append((units[j],no_machines))
          index+=1
      n+=1
      gl_list.append(sub_list)
      if i == units_len-1:
        break
  assign_low=compute(gl_list[0],country)
  machine = gl_list[0]
  for sub in gl_list:
    current=compute(sub,country)
    if current < assign_low:
      assign_low = current
      machine = sub



  region_dict={'region':country,'total_cost':'${}'.format(assign_low),'machines':label_conversion(machine)}
  report['Output'].append(region_dict)
  

def compute(sub,country):
  val=0
  for unit,no in sub:
    index=units.index(unit)
    val=val+countries[country][index]*hour*no
  return val

def label_conversion(machine):
  label=[]
  for unit,no in machine:
    index=units.index(unit)
    label.append((machines[index],no))
  return label

if __name__ == "__main__":
  hour=int(input("Enter Hour: "))
  capacity=int(input("Enter Machine capacity: "))
  if hour == 0 or capacity == 0:
    print("Please Enter correct Input") 
  elif capacity % 10 != 0:
    print("Please check capacity value,it will always be multiple of 10 ")
  else:
    machines=['Large','XLarge','2XLarge','4XLarge','8XLarge','10XLarge']
    units=[10,20,40,80,160,320]
    units_len = len(units)
    countries={'India':[140,None,413,890,1300,2970],'New York':[120,230,450,774,1400,2820],'China':[110,200,None,670,1180,None]}
    report={'Output':[]}
    for name in countries.keys():
      perform(name)
    print(report)
    