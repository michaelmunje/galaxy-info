import pytest
from galana import models
import os


def test_default_paths():
    model_paths = models.initialize_default_paths()
    assert(model_paths.test_image_path == os.getcwd() + '/data/test_images/')
    assert(model_paths.valid_image_path == os.getcwd() + '/data/valid_images/')
    assert(model_paths.train_image_path == os.getcwd() + '/data/images_training_rev1/')
    assert(model_paths.test_image_files == [])
    assert(model_paths.train_image_files == [])
    assert(model_paths.valid_image_files == [])

    assert(model_paths.all_solutions == os.getcwd() + '/data/solutions/training_solutions_rev1.csv')
    assert(model_paths.clean_solutions == os.getcwd() + '/data/solutions/clean_solutions.csv')

    assert(model_paths.clean_train_solutions == os.getcwd() + '/data/solutions/train_clean_solutions.csv')
    assert(model_paths.augmented_train_solutions == os.getcwd() + '/data/solutions/train_augmented_solutions.csv')

    assert(model_paths.test_file == os.getcwd() + '/data/all_zeros_benchmark.csv')
    assert(model_paths.output_model_file == os.getcwd() + '/data/models/galaxy_classifier_model.json')
    assert(model_paths.output_model_weights == os.getcwd() + '/data/models/galaxy_classifier_weights.h5')

    assert(model_paths.checkpoint_path == os.getcwd() + "/data/models/checkpoints/{epoch:02d}-{val_acc:.2f}.hdf5")
    assert(model_paths.checkpoint_overall_path == os.getcwd() + "/data/models/best_overall_model.hdf5")

    assert(model_paths.valid_conf_matrix == os.getcwd() + "/data/eval/valid_conf_matrix.csv")
    assert(model_paths.valid_other_metrics == os.getcwd() + "/data/eval/valid_other_metrics.csv")

    assert(model_paths.test_conf_matrix == os.getcwd() + "/data/eval/test_conf_matrix.csv")
    assert(model_paths.test_other_metrics == os.getcwd() + "/data/eval/test_other_metrics.csv")

    assert(model_paths.valid_true == os.getcwd() + "/data/eval/valid/true.csv")
    assert(model_paths.valid_preds == os.getcwd() + "/data/eval/valid/preds.csv")

    assert(model_paths.test_true == os.getcwd() + "/data/eval/test/true.csv")
    assert(model_paths.test_preds == os.getcwd() + "/data/eval/test/preds.csv")


def test_custom_paths():
    model_paths = models.initialize_custom_paths(test_images_p="asdf", train_images_p="gggg", valid_images_p="gggg", train_sol='1234', clean_sols='pl', augmented_sols='hello',
                                                 valid_sols='bbb', test_sols='ccc',
                                                 test_f='wswqsas/wdowdw.pt', output_model_f='ssqqas/wdowdw.pt', output_model_w='wwswqa/wdowdw.pt',
                                                 checkpoint_p='aaaa/aaaa.a', valid_conf_matrix='c.c', valid_other_metrics='a', test_conf_matrix='c.c', test_other_metrics='a',
                                                 checkpoint_p_overall='aaaa/aaab.a', val_true='bb', val_preds='c.c', test_true='bb', test_preds='c.c')
    assert(model_paths.test_image_path == "asdf")
    assert(model_paths.train_image_path == "gggg")
    assert(model_paths.valid_image_path == "gggg")
    assert(model_paths.test_image_files == [])
    assert(model_paths.train_image_files == [])
    assert(model_paths.all_solutions == '1234')
    assert(model_paths.clean_train_solutions == 'pl')
    assert(model_paths.augmented_train_solutions == 'hello')
    assert(model_paths.valid_solutions == 'bbb')
    assert(model_paths.test_solutions == 'ccc')
    assert(model_paths.test_file == 'wswqsas/wdowdw.pt')
    assert(model_paths.output_model_file == 'ssqqas/wdowdw.pt')
    assert(model_paths.output_model_weights == 'wwswqa/wdowdw.pt')
    assert(model_paths.checkpoint_path == 'aaaa/aaaa.a')
    assert(model_paths.checkpoint_overall_path == 'aaaa/aaab.a')
    assert(model_paths.valid_true == 'bb')
    assert(model_paths.valid_preds == 'c.c')
    assert(model_paths.test_true == 'bb')
    assert(model_paths.test_preds == 'c.c')
    assert(model_paths.valid_conf_matrix == 'c.c')
    assert(model_paths.valid_other_metrics == 'a')
    assert(model_paths.test_conf_matrix == 'c.c')
    assert(model_paths.test_other_metrics == 'a')


if __name__ == '__main__':
    pytest.main([__file__])
