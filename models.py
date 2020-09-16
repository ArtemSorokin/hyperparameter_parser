X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)
xg_reg.fit(X_train,y_train)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.5, learning_rate = 0.0001, n_estimators = 10)
xg_reg.fit(X_train,y_train)

X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
regr = svm.SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,coef0=1)
regr.fit(X, y)

