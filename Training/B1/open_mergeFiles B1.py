import os
filenames = ['B2_texto1.txt', 'B2_texto2.txt', 'B2_texto3.txt','B2_texto4.txt','B2_texto5.txt','B2_texto6.txt','B2_texto7.txt','B2_texto8.txt','B2_texto9.txt','B2_texto10.txt','B2_texto11.txt','B2_texto12.txt','B2_texto13.txt','B2_texto1.txt','B2_texto14.txt','B2_texto15.txt','B2_texto16.txt','B2_texto17.txt','B2_texto18.txt','B2_texto19.txt','B2_texto20.txt','B2_texto21.txt','B2_texto22.txt','B2_texto23.txt','B2_texto24.txt','B2_texto25.txt','B2_texto26.txt','B2_texto27.txt','B2_texto28.txt','B2_texto29.txt','B2_texto30.txt','B2_texto31.txt','B2_texto32.txt','B2_texto33.txt','B2_texto34.txt','B2_texto35.txt','B2_texto35.txt','B2_texto36.txt','B2_texto37.txt', 'B2_texto38.txt', 'B2_texto39.txt', 'B2_texto40.txt','B2_texto41.txt','B2_texto42.txt','B2_texto43.txt','B2_texto44.txt','B2_texto45.txt','B2_texto46.txt','B2_texto47.txt','B2_texto48.txt','B2_texto49.txt','B2_texto50.txt','B2_texto51.txt','B2_texto52.txt','B2_texto53.txt','B2_texto54.txt','B2_texto55.txt','B2_texto56.txt','B2_texto57.txt','B2_texto58.txt','B2_texto59.txt','B2_texto60.txt','B2_texto61.txt','B2_texto62.txt','B2_texto63.txt','B2_texto64.txt','B2_texto65.txt','B2_texto66.txt','B2_texto67.txt','B2_texto68.txt','B2_texto69.txt','B2_texto70.txt','B2_texto71.txt','B2_texto72.txt','B2_texto73.txt','B2_texto74.txt','B2_texto75.txt','B2_texto76.txt','B2_texto77.txt', 'B2_texto78.txt', 'B2_texto79.txt','B2_texto80.txt','B2_texto81.txt','B2_texto82.txt','B2_texto83.txt','B2_texto84.txt','B2_texto85.txt','B2_texto86.txt','B2_texto87.txt','B2_texto88.txt','B2_texto89.txt','B2_texto90.txt','B2_texto91.txt','B2_texto92.txt','B2_texto93.txt','B2_texto94.txt','B2_texto95.txt','B2_texto96.txt','B2_texto97.txt','B2_texto98.txt','B2_texto99.txt','B2_texto100.txt','B2_texto101.txt','B2_texto102.txt','B2_texto103.txt','B2_texto104.txt','B2_texto105.txt','B2_texto106.txt','B2_texto107.txt','B2_texto108.txt','B2_texto109.txt','B2_texto110.txt','B2_texto111.txt','B2_texto112.txt','B2_texto113.txt','B2_texto114.txt','B2_texto115.txt','B2_texto116.txt', 'B2_texto117.txt', 'B2_texto118.txt','B2_texto119.txt','B2_texto120.txt','B2_texto121.txt','B2_texto122.txt','B2_texto123.txt','B2_texto124.txt','B2_texto125.txt']

#path=r"C:/Users/user/Dropbox/Eric/Vrep_python_working_folder/b2"
##working_directory = os.getcwd()
##
##files = os.listdir(working_directory)  # Get all the files in that directory
##print("Files in %r: %s" % (working_directory, files))
##print("Working dir:",working_directory)






with open('B2_output_file', 'w',encoding="utf-8") as outfile:
    for fname in filenames:
         with open(fname,encoding="utf-8") as infile:
             outfile.write(infile.read())
         outfile.write('\n\n\n\n')
