import argparse

def get_parser():

    parser = argparse.ArgumentParser(description='tri-joint parameters')
    # general
    parser.add_argument('--seed', default=1234, type=int)
    parser.add_argument('--no-cuda', action='store_true')

    # data
    parser.add_argument('--img_path', default='data/images/')
    parser.add_argument('--data_path', default='data/')
    parser.add_argument('--workers', default=10, type=int)

    # model
    parser.add_argument('--batch_size', default=100, type=int)
    parser.add_argument('--snapshots', default='snapshots/',type=str)

    # im2recipe model
    parser.add_argument('--embDim', default=1024, type=int)
    parser.add_argument('--nRNNs', default=1, type=int)
    parser.add_argument('--srnnDim', default=1024, type=int)
    parser.add_argument('--irnnDim', default=300, type=int)
    parser.add_argument('--imfeatDim', default=2048, type=int)
    parser.add_argument('--stDim', default=1024, type=int)
    parser.add_argument('--ingrW2VDim', default=300, type=int)
    parser.add_argument('--maxSeqlen', default=20, type=int)
    parser.add_argument('--maxIngrs', default=20, type=int)
    parser.add_argument('--maxImgs', default=5, type=int)
    parser.add_argument('--numClasses', default=1005, type=int)
    parser.add_argument('--preModel', default='resNet50',type=str)
    parser.add_argument('--semantic_reg', default=True,type=bool)
    # parser.add_argument('--semantic_reg', default=False,type=bool)
    parser.add_argument('--modality_alignment', default=True, type=bool)
    parser.add_argument('--use_soft_margin', default=True, type=bool)
    parser.add_argument('--use_cat_triplet_loss', default=True, type=bool)
    parser.add_argument('--use_circle_loss', default=True, type=bool)

    # training 
    parser.add_argument('--lr', default=0.0001, type=float)
    parser.add_argument('--momentum', default=0.9, type=float)
    parser.add_argument('--weight_decay', default=0, type=float)
    parser.add_argument('--epochs', default=500, type=int)
    parser.add_argument('--start_epoch', default=0, type=int)
    parser.add_argument('--ingrW2V', default='data/text/vocab.bin',type=str)
    parser.add_argument('--valfreq', default=10,type=int)  
    parser.add_argument('--patience', default=1, type=int)
    parser.add_argument('--freeVision', default=False, type=bool)
    parser.add_argument('--freeRecipe', default=True, type=bool)
    # parser.add_argument('--cos_weight', default=0.98, type=float)
    # parser.add_argument('--cls_weight', default=0.01, type=float)
    parser.add_argument('--sr_img_weight', default=0.005, type=float)
    parser.add_argument('--sr_rec_weight', default=0.005, type=float)
    parser.add_argument('--ma_weight', default=0.005, type=float)
    parser.add_argument('--resume', default='', type=str)
    parser.add_argument('--gama', default=16, type=int)
    parser.add_argument('--margin', default=0.0, type=float)
    parser.add_argument('--cat_triplet_weight', default=0.5, type=float)
    # test
    parser.add_argument('--path_results', default='results/', type=str)
    parser.add_argument('--result_dir', default='sm_05double_tri', type=str)
    # MedR / Recall@1 / Recall@5 / Recall@10
    parser.add_argument('--embtype', default='image', type=str) # [image|recipe] query type
    parser.add_argument('--medr', default=1000, type=int)

    # dataset
    parser.add_argument('--maxlen', default=20, type=int)
    parser.add_argument('--vocab', default = 'data/text/vocab.txt', type=str)
    parser.add_argument('--dataset', default = 'data/recipe1M/', type=str)
    parser.add_argument('--sthdir', default = 'data/', type=str)

    return parser




