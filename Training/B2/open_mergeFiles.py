import os
filenames = ['A1_texto1.txt', 'A1_texto2.txt', 'A1_texto3.txt','A1_texto4.txt','A1_texto5.txt','A1_texto6.txt','A1_texto7.txt','A1_texto8.txt','A1_texto9.txt','A1_texto10.txt','A1_texto11.txt','A1_texto12.txt','A1_texto13.txt','A1_texto14.txt','A1_texto15.txt','A1_texto16.txt','A1_texto17.txt','A1_texto18.txt','A1_texto19.txt','A1_texto20.txt','A1_texto21.txt','A1_texto22.txt','A1_texto23.txt','A1_texto24.txt','A1_texto25.txt','A1_texto26.txt','A1_texto27.txt','A1_texto28.txt','A1_texto29.txt','A1_texto30.txt','A1_texto31.txt','A1_texto32.txt','A1_texto33.txt','A1_texto34.txt','A1_texto35.txt','A1_texto35.txt','A1_texto36.txt','A1_texto37.txt', 'A1_texto38.txt', 'A1_texto39.txt', 'A1_texto40.txt','A1_texto41.txt','A1_texto42.txt','A1_texto43.txt','A1_texto44.txt','A1_texto45.txt','A1_texto46.txt','A1_texto47.txt','A1_texto48.txt','A1_texto49.txt','A1_texto50.txt','A1_texto51.txt','A1_texto52.txt','A1_texto53.txt','A1_texto54.txt','A1_texto55.txt','A1_texto56.txt','A1_texto57.txt','A1_texto58.txt','A1_texto59.txt','A1_texto60.txt','A1_texto61.txt','A1_texto62.txt','A1_texto63.txt','A1_texto64.txt','A1_texto65.txt','A1_texto66.txt','A1_texto67.txt','A1_texto68.txt','A1_texto69.txt','A1_texto70.txt','A1_texto71.txt','A1_texto72.txt','A1_texto73.txt','A1_texto74.txt','A1_texto75.txt','A1_texto76.txt','A1_texto77.txt', 'A1_texto78.txt', 'A1_texto79.txt','A1_texto80.txt','A1_texto81.txt','A1_texto82.txt','A1_texto83.txt','A1_texto84.txt','A1_texto85.txt','A1_texto86.txt','A1_texto87.txt','A1_texto88.txt','A1_texto89.txt','A1_texto90.txt','A1_texto91.txt','A1_texto92.txt','A1_texto93.txt','A1_texto94.txt','A1_texto95.txt','A1_texto96.txt','A1_texto97.txt','A1_texto98.txt','A1_texto99.txt','A1_texto100.txt','A1_texto101.txt','A1_texto102.txt','A1_texto103.txt','A1_texto104.txt','A1_texto105.txt','A1_texto106.txt','A1_texto107.txt','A1_texto108.txt','A1_texto109.txt','A1_texto110.txt','A1_texto111.txt','A1_texto112.txt','A1_texto113.txt','A1_texto114.txt','A1_texto115.txt','A1_texto116.txt', 'A1_texto117.txt', 'A1_texto118.txt','A1_texto119.txt','A1_texto120.txt','A1_texto121.txt','A1_texto122.txt','A1_texto123.txt','A1_texto124.txt','A1_texto125.txt']

#path=r"C:/Users/user/Dropbox/Eric/Vrep_python_working_folder/b2"
##working_directory = os.getcwd()
##
##files = os.listdir(working_directory)  # Get all the files in that directory
##print("Files in %r: %s" % (working_directory, files))
##print("Working dir:",working_directory)


path=os.getcwd()
print(path)
             
os.chdir(r"C:\Users\user\Dropbox\Eric\Vrep_python_working_folder\A1")

path=os.getcwd()
print(path)



with open('A1_output_file', 'w',encoding="utf-8") as outfile:
    for fname in filenames:
         with open(fname,encoding="utf-8") as infile:
             outfile.write(infile.read())
         outfile.write('\n\n\n\n')
