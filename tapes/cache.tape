task cache : hiertype
  < data=@
  > dump
  :: contextualizer=@ :: unit=@ :: layers=@
  :: grid=@
  :: gpuId=@
{
  mkdir -p $dump/cfet/
  for partition in train crowd_dev crowd_test; do
    PYTHONPATH=$hiertype CUDA_VISIBLE_DEVICES=$gpuId \
    python $hiertype/hiertype/commands/cache_repr.py \
     --input $data/cfet/${partition}.tsv --output $dump/cfet/${partition}.db \
     --model $contextualizer \
     --unit $unit \
     --layers $layers
  done
}

task cache_predict : hiertype
  < data=@
  > dump
  :: contextualizer=@ :: unit=@ :: layers=@
  :: grid=@
  :: gpuId=@
{
  mkdir -p $dump
  for partition in {0..19}; do
    PYTHONPATH=$hiertype CUDA_VISIBLE_DEVICES=$gpuId \
    python $hiertype/hiertype/commands/cache_repr.py \
     --input $data/cfet/webhose_arg_${partition}.tsv --output $dump/cfet/webhose_arg_${partition}.db \
     --model $contextualizer \
     --unit $unit \
     --layers $layers
  done

  for partition in {0..19}; do
    PYTHONPATH=$hiertype CUDA_VISIBLE_DEVICES=$gpuId \
    python $hiertype/hiertype/commands/cache_repr.py \
     --input $data/cfet/webhose_ner_${partition}.tsv --output $dump/cfet/webhose_ner_${partition}.db \
     --model $contextualizer \
     --unit $unit \
     --layers $layers
  done
}
