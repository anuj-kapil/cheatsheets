getwd()
library(data.table)
library(lubridate)
library(ggplot2)
library(stringr)
# Data Structures

# Create a vector (numeric array)
vec1 <- c(2,3,5,7)
vec2 <- c(3,5,1,4)
vec1 + vec2
# Create a matrix
mtrx1 <- matrix(vec1, nrow = 2, ncol = 2)
mtrx2 <- matrix(vec2, nrow = 2, ncol = 2)
mtrx1 + mtrx2
# Create a character array
names_array <- c('Jon','Jane','John','Jean')

# Create a list
lst <- list(id = vec1, name = names_array)

# Create a data.frame
df <- data.frame(id = vec1, name = names_array)

# Create a data.table
dt <- data.table(id = vec1, name = names_array)

# Data Export and Import
output_dir <- file.path(getwd(), 'Data')

if (!dir.exists(output_dir)){
  dir.create(output_dir)
} else {
  print("Dir already exists!")
}

fwrite(dt,'Data/employees.csv')

dt_r <- fread('Data/employees.csv')

# Parsing web-pages

# Data Binding

# Bind new columns
age <- c(30, 25, 35, 29)
height <- c(1.7, 1.8, 1.65, 1.85)
dt_r <- cbind(dt_r, age)
dt_r <- cbind(dt_r, height)

# Bind new rows
# new row is defined as a new data.table
new_row <- data.table(id = 9, name = 'Jen', age = 31, height = 1.6)

# Must be of same shape
dt_r <- rbind(dt_r, new_row)


# Data Wrangling

## Descriptive statistics
summary(dt_r)

## Removing NULLS
dt_r[!is.na(name)]

## Removing Duplicates
unique(address_dt)

## Select rows/columns
### Rows
dt_r[1:2,]
dt_r[name=='Jon',]

### Columns
dt_r[,1:2]
dt_r[,.(name, id)]

### Rows & Columns
dt_r[name=='Jon',.(name, id)]

## Where clause
## group by
## order by

weight <- c(75,60,70,65,50)
dt_r <- cbind(dt_r, weight)

gender <- c('M','F','M','F','F')
dt_r <- cbind(dt_r, gender)

dt_r[weight>60, .N, by =  gender][order(-N)]

# Data Transformation

# Convert height in metres to inches and save as another column

dt_r[, height_inch:=height*39.37]

# Drop a column
dt_r[, height_inch:= NULL]

# Long form

dt_r <- melt(dt_r, id.vars = 'name', measure.vars = c('id','age','height','height_inch'))

# Wide form
dt_r <- dcast(dt_r, name~variable, value.var = 'value')

#Data Join and Rolling Join

address_id <- c(1,2,3,4,5)
address_array <- c('1640 Riverside Drive, Hill Valley, California'
                   ,'344 Clinton St., Apt. 3B, Metropolis, USA'
                   ,'12 Grimmauld Place, London, UK'
                   ,'221B Baker Street, London, UK'
                   ,'1313 Webfoot Walk, Duckburg, Calisota')

address_dt <- data.table(address_id = address_id, address = address_array)

address_id <- c(1,2,3,5,5)
dt_r <- cbind(dt_r, address_id)

setkey(dt_r, address_id)
setkey(address_dt, address_id)

dt_r[address_dt]
merge(dt_r,address_dt, all.x=TRUE)

dt_r[address_dt,  nomatch=0]
address_dt[dt_r]

# String Manipulation
str_detect()
dt_r[,.(name, o_exists = str_detect(name, 'o'))]


dt_r[,.(name, first_letter = str_sub(name, 1,1), last_letter = str_sub(name, -1,-1))]

#dt_r[,.(o_names = str_subset(name, 'o'))]

# Regex

dt_r[,str_view_all(name,'n')]
dt_r[,str_view_all(name,'n$')]
dt_r[,str_view_all(name,'^J')]


# Date and Time

birth_date <- c('1987-03-01','1990-10-09','2000-07-15','1984-05-01','2001-06-03')
dt_r <- cbind(dt_r, birth_date)
summary(dt_r)
dt_r[,birth_date:= as.IDate(birth_date)]
summary(dt_r)
dt_r[,birth_date:= as.numeric(birth_date)]
as.numeric()

# Data Visualization


ggplot(dt_r, aes(x=height, y=weight, color = gender))+
  geom_point()



