import csv
import re
import sys

#def convertESRI2TableauFormat( p_inputfile, p_outputfile):

l_outfileName = 'c:/ESRI_suburb_tab_format.csv'  # make changes here..
l_ESRIFileName ='c:/ESRI_suburb.csv'             # make changes here..

rdx=0
csv.field_size_limit(sys.maxsize)
outfile = open( l_outfileName, 'w', newline='')
csvWriter = csv.writer( outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

with open( l_ESRIFileName, 'r') as csvfile:

 csvR = csv.reader( csvfile, delimiter=',', quotechar='"')
 for row in csvR:
    rdx += 1           
    ci=0
    rowValues = []
    rowValues.append(row[1]);# ssc_code
    rowValues.append(row[2]);# ssc_name
    rowValues.append(row[4]);# state_code
    rowValues.append(row[5]);# confidence
    rowValues.append(row[6].strip());# AREA_SQKM
    rowValues.append('');# place holder for lat
    rowValues.append('');# place holder for long
    rowValues.append('');# place holder for polygon
    rowValues.append('');# place holder for point
      
    if ( rdx==1): # first row add header col names

       rowValues[5]=('Latitude');# 
       rowValues[6]=('Longitude');#
       rowValues[7]=('Polygon_ID');#
       rowValues[8]=('Point_ID');#
       csvWriter.writerow( rowValues);
    else:        
       for col in row:

           ci += 1
           LatLonStrArr=[]

           if (ci==1): # first col has the polygon values.

               polygonArr = []
               polygonArr = re.findall('(\((?:-?\d+\.\d+\s-?\d+\.\d+,?)+\))', col)
               polyx =0
                     
               for px in polygonArr:

                   polyx += 1
                   LatLonStrArr = []
                   LatLonStrArr = re.findall('(-?\d+\.\d+\s-?\d+\.\d+)', px)

                   if( len( LatLonStrArr) != 0 ):

                       pointx  = 0
                       pointxx = 0
                       for lx in LatLonStrArr:

                           pointx += 1
                           resArr = re.findall( '(-?\d+\.\d+)', lx)
                           #print('&gt;&gt;&gt;&gt; lx='+lx + "/"+ str(len(resArr)))
                           rowValues[5] = resArr[1] # lat
                           rowValues[6] = resArr[0] #long
                           rowValues[7] = polyx

                           if( (pointx ==1) | (pointx == len(LatLonStrArr))| (len(LatLonStrArr)&lt;=10)| (pointx % 10 == 0) ):
                              pointxx += 1
                              rowValues[8] = pointxx
                              csvWriter.writerow( rowValues);
   
    #print('ROW========================='+ str(rdx))
    #for rx in rowValues:
    #   print('val=' + str(rx))
    
    #if (rdx &gt;=100):
       #break
            
csvfile.close()
outfile.close()