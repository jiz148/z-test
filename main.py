import numpy as np

from common.z_table import calculate_p_from_z

if __name__ == "__main__":
    # let's say that a kind of
    # tree is known to have average life span of 40 years

    # create sample
    mu = 40
    ages_list = [40, 80, 43, 28, 17, 74] * 30
    ages_list_2 = [100, 104, 85, 99, 150, 200] * 30
    ages = np.array(ages_list_2)

    # calculate z-statistic
    avg = np.average(ages)
    sd = np.std(ages)
    z = (avg - mu) / sd
    print('z-statistic is ', z)

    # calculate p-value
    p = calculate_p_from_z(z)
    print('p-value is ', p)
    print('so, assuming H0, there is {} of chance we would obtain the sample we got'.format(p))
