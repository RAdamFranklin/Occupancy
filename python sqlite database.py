import sqlite3
conn = sqlite3.connect('database1.db')
c = conn.cursor()
# t values are grid-eye data points
# CO2 is CO2 data
# temp is tempurature data
# humid is humidity data
# time is time of sampled data
c.execute('CREATE TABLE Data (t1 real, t2 real, t3 real, t4 real, t5 real, t6 real, t7 real, t8 real, t9 real, t10 real, t11 real, t12 real, t13 real, t14 real, t15 real, t16 real, t17 real, t18 real, t19 real, t20 real, t21 real, t22 real, t23 real, t24 real, t25 real, t26 real, t27 real, t28 real, t29 real, t30 real, t31 real, t32 real, t33 real, t34 real, t35 real, t36 real, t37 real, t38 real, t39 real, t40 real, t41 real, t42 real, t43 real, t44 real, t45 real, t46 real, t47 real, t48 real, t49 real, t50 real, t51 real, t52 real, t53 real, t54 real, t55 real, t56 real, t57 real, t58 real, t59 real, t60 real, t61 real, t62 real, t63 real, t64 real, CO2 real, temp real, humid real, time real)')
conn.commit()
conn.close()