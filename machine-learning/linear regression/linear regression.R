##
## Simple Linear Regression
##

# Initializing Training data x,y

x <- c(2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0)
y <- c(5.1,6.1,6.9,7.8,9.2,9.9,11.5,12,12.8)


# Modeling Y as a linear function of X
res <- lm( y ~ x )
print(res)


##
## Call:
## lm(formula = y ~ x)

## Coefficients:
##  (Intercept)            x  
##        1.060        1.993 
##


# Plotting the training data and the model
plot(x,y, col='red', main='Linear regression')
abline(res, col='blue')

# Squared error cost function
cost <- function(X, y, theta_value) {
  sum( (X %*% theta_value - y)^2 ) / (2*length(y))
}

# Initializing learning rate and iteration limit
alpha_value       <- 0.001
total_iterations  <- 500


# Cost and Theta history
cost_history <- double(total_iterations)
theta_history <- list(total_iterations)

# Initializing the coefficients
theta_value <- matrix(c(0,0), nrow=2)

# add a column of 1's for the intercept coefficient
X <- cbind(1, matrix(x))

# gradient descent
for (i in 1:total_iterations) {
  error <- (X %*% theta_value - y)
  delta_Value <- t(X) %*% error / length(y)
  theta_value <- theta_value - alpha_value * delta_Value
  cost_history[i] <- cost(X, y, theta_value)
  theta_history[[i]] <- theta_value
}

# Converging fit and ploting data
plot(x,y, col=rgb(0.2,0.4,0.6,0.4), main='Linear regression by gradient descent')
for (i in c(1,3,6,10,14,seq(20,total_iterations,by=10))) {
  abline(coef=theta_history[[i]], col=rgb(0.8,0,0,0.3))
}
abline(coef=theta_value, col="blue")

# Plotting J for the learning duration
cost_history[seq(1,total_iterations, by=100)]
plot(cost_history, type='l', col='blue', lwd=2, main='Plotting J for the learning duration', ylab='Cost', xlab='Iterations')

