#! /usr/bin/python

import getopt
import sys


def deal_args(my_argv):
    v, n1, n0, b, e, t, z = False, 200, 200, 30, 1000, 8, 1000
    m = 'lenet'
    try:
        opts, args = getopt.getopt(my_argv, "vhy:n:b:e:t:z:m:",
                                   ["p_sample_size=", "n_sample_size=", "batch_size=", "epoch_num=", "thread_num=",
                                    'test_size=', 'network_model='])
    except getopt.GetoptError:
        print 'command -v -y <p_sample_size> -n <n_sample_size> -b <batch_size> -e <epoch_num> -t <thread_num>, ' \
              '-z <test_size>, -m <network_model>'
        print 'default settings: v=%s, d=%s, n1=%d, n0=%d, b=%d, e=%d, t=%d, z=%d, m=%s' % (
            v, n1, n0, b, e, t, z, m)
    for opt, arg in opts:
        if opt == '-h':
            print 'command -v -y <p_sample_size> -n <n_sample_size> -b <batch_size> -e <epoch_num> -t <thread_num>, ' \
                  '-z <test_size>, -m <network_model>'
            sys.exit()
        elif opt == '-v':
            v = True
        elif opt in ("-y", "--p_sample_size"):
            n1 = int(arg)
        elif opt in ("-n", "--n_sample_size"):
            n0 = int(arg)
        elif opt in ("-b", "--batch_size"):
            b = int(arg)
        elif opt in ("-e", "--epoch_num"):
            e = int(arg)
        elif opt in ("-t", "--thread_num"):
            t = int(arg)
        elif opt in ("-z", "--test_size"):
            z = int(arg)
        elif opt in ("-m", "--network_model"):
            m = arg
    print 'settings: v=%s, n1=%d, n0=%d, b=%d, e=%d, t=%d, z=%d, m=%s' % (
        v, n1, n0, b, e, t, z, m)
    return v, n1, n0, b, e, t, z, m


def deal_args_active(my_argv):
    v, n1, n0, b, e, t, z, a, u, l, a_c = False, 200, 200, 30, 1000, 8, 1000, 50, 0.55, 0.45, 10000
    m = 'lenet'
    try:
        opts, args = getopt.getopt(my_argv, "vhy:n:b:e:t:z:m:a:u:l:c:",
                                   ["p_sample_size=", "n_sample_size=", "batch_size=", "epoch_num=", "thread_num=",
                                    'test_size=', 'network_model=', 'active_size=', 'threshold_up=', 'threshold_low=',
                                    'active_cache='])
    except getopt.GetoptError:
        print 'command -v -y <p_sample_size> -n <n_sample_size> -b <batch_size> -e <epoch_num> -t <thread_num>, ' \
              '-z <test_size>, -m <network_model>, -a <active_size>, -u <threshold_up>, -l <threshold_low>, ' \
              '-c <active_cache> '
        print 'default settings: v=%s, n1=%d, n0=%d, b=%d, e=%d, t=%d, z=%d, m=%s, a=%d, u=%f, l=%f, c=%d' % (
            v, n1, n0, b, e, t, z, m, a, u, l, a_c)
    for opt, arg in opts:
        if opt == '-h':
            print 'command -v -y <p_sample_size> -n <n_sample_size> -b <batch_size> -e <epoch_num> -t <thread_num>, ' \
                  '-z <test_size>, -m <network_model>, -a <active_size>, -u <threshold_up>, -l <threshold_low>, ' \
                  '-c <active_cache> '
            sys.exit()
        elif opt == '-v':
            v = True
        elif opt in ("-y", "--p_sample_size"):
            n1 = int(arg)
        elif opt in ("-n", "--n_sample_size"):
            n0 = int(arg)
        elif opt in ("-b", "--batch_size"):
            b = int(arg)
        elif opt in ("-e", "--epoch_num"):
            e = int(arg)
        elif opt in ("-t", "--thread_num"):
            t = int(arg)
        elif opt in ("-z", "--test_size"):
            z = int(arg)
        elif opt in ("-m", "--network_model"):
            m = arg
        elif opt in ("-a", "--active_size"):
            a = int(arg)
        elif opt in ("-u", "--threshold_up"):
            u = float(arg)
        elif opt in ("-l", "--threshold_low"):
            l = float(arg)
        elif opt in ("-c", "--active_cache"):
            a_c = int(arg)
    print 'settings: v=%s, n1=%d, n0=%d, b=%d, e=%d, t=%d, z=%d, m=%s, a=%d, u=%f, l=%f, c=%d' % (
        v, n1, n0, b, e, t, z, m, a, u, l, a_c)
    return v, n1, n0, b, e, t, z, m, a, u, l, a_c
