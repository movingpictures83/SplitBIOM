#exec(open("plugins/SplitBIOM/example/all.py").read())

class SplitBIOMPlugin:
   def input(self, inputfile):
      exec(open("plugins/SplitBIOM/example/all.py").read())
      #exec(open(inputfile).read())

   def run(self):
     self.levels = ["kingdom", "phylum", "class", "order", "family", "genus", "species"]
     self.phylo_tree = dict()
     for level in self.levels:
        self.phylo_tree[level] = dict()

     for i in range(0, len(self.myBIOM["rows"])):
        while (len(self.myBIOM["rows"][i]["metadata"]["taxonomy"]) < 6):
           self.myBIOM["rows"][i]["metadata"]["taxonomy"].append("Other")

   def output(self, outputfile):

     ########################################################
     for i in range(0, len(self.levels)):
      level = self.levels[i]
      for triplet in self.myBIOM["data"]:
        otu, sample, count = triplet[0], triplet[1], triplet[2]
        if (len(self.myBIOM["rows"][otu]["metadata"]["taxonomy"]) >= i+1):
         tax = ""
         for j in range(0, i+1):
           tax += self.myBIOM["rows"][otu]["metadata"]["taxonomy"][j]
         if (tax not in self.phylo_tree[level].keys()):
           self.phylo_tree[level][tax] = [ [0] * len(self.myBIOM["columns"]), self.myBIOM["rows"][otu]["metadata"]["taxonomy"][0:i+1] ]
         self.phylo_tree[level][tax][0][sample] += count

      self.data_to_print = []
      self.rows_to_print = []
      otuid = 0
      for key in self.phylo_tree[level]:
        value = self.phylo_tree[level][key]
        self.rows_to_print.append({"id": "OTU"+str(otuid), "metadata":{"taxonomy": value[1]}})
        for sampleid in range(0, len(value[0])):
           self.data_to_print.append([otuid, sampleid, value[0][sampleid]])
        otuid += 1   

      self.header_order = ["id", "format", "format_url", "type", "generated_by", "date", "matrix_type", "matrix_element_type"]

      outfile = open(outputfile+"."+level+".biom", 'w')
      outfile.write("{")
      for i in range(0, len(self.header_order)):
       outfile.write("\""+self.header_order[i]+"\":\""+self.myBIOM[self.header_order[i]]+"\",",)
      outfile.write("\"shape\":"+str([len(self.rows_to_print), len(self.myBIOM["columns"])])+",")
      outfile.write("\"data\":"+str(self.data_to_print).replace('\'', '\"')+",")
      outfile.write("\"rows\":"+str(self.rows_to_print).replace('\'', '\"')+",")
      outfile.write("\"columns\":"+str(self.myBIOM["columns"]).replace('\'', '\"')+"}\n") 
      ########################################################





########################################################
# PRINTS SAME ONE AS INPUT
#key_order = ["id", "format", "format_url", "type", "generated_by", "date", "matrix_type", "matrix_element_type", "shape", "data", "rows", "columns"]
#print "{",
#for i in range(0, len(key_order)):
#   print "\""+key_order[i]+"\":",
#   if (i < len(key_order)-4):
#      print "\""+self.myBIOM[key_order[i]]+"\"",
#   else:
#      print self.myBIOM[key_order[i]],
#   if (i != len(key_order)-1):
#      print ",",
#print "}"
########################################################
