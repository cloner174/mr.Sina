library(dplyr)

node <- read.csv("data/node_data.csv")

link <- read.csv("links.csv")

head(link)

node <- as.data.frame(node)
link <- as.data.frame(link)

which( link$source == 27 ) 

node$X_igraph_index

dim(link)[1]

V <- node$X_igraph_index


VV <- list()
for (i in c(1:702)) {
  VV[[i]] <- which(link$source == V[i] | link$target == V[i])
}



LL <- vector()
for (i in c(1:702)) {
  temp <- VV[[i]]
  for (j in temp) {
    LL <- c(LL, j)
  }
}


link_data <- link[LL,]


link_data

write.csv(link_data, 'output/link_data.csv')
