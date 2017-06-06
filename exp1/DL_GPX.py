#! /usr/bin/python

import sys
import gc
import DL_OSM

sys.path.append("../lib")
import NN_Model
import OSM

evaluate_only, tr_n1, tr_n0, tr_b, tr_e, tr_t, cv_i, te_n, nn = DL_OSM.deal_args(sys.argv[1:])
cv_n = 4

print '--------------- Read Samples ---------------'
client = OSM.GPXclient()
train_imgs, test_imgs = client.imgs_cross_validation(cv_i, cv_n)
osm_p_imgs = client.read_p_images()
osm_n_imgs = client.read_n_images()
print 'train_imgs: %d \n' % len(train_imgs)
print 'osm_p_imgs: %d \n' % len(osm_p_imgs)
print 'osm_n_imgs: %d\n' % len(osm_n_imgs)
img_X, Y = DL_OSM.read_train_sample(tr_n1, tr_n0, train_imgs, osm_p_imgs, osm_n_imgs)
m = NN_Model.Model(img_X, Y, nn + '_ZY')

if not evaluate_only:
    print '--------------- Training on GPX Labels---------------'
    m.set_batch_size(tr_b)
    m.set_epoch_num(tr_e)
    m.set_thread_num(tr_t)
    m.train(nn)
    print '--------------- Evaluation on Training Samples ---------------'
    m.evaluate()
del img_X, Y, train_imgs
gc.collect()

print '--------------- Evaluation on GPX Samples ---------------'
osm_p_imgs = client.read_p_images()
osm_n_imgs = client.read_n_images()
img_X2, Y2 = DL_OSM.read_test_sample(te_n, test_imgs, osm_p_imgs, osm_n_imgs)
m.set_evaluation_input(img_X2, Y2)
m.evaluate()