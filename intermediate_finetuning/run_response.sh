CUDA_VISIBLE_DEVICES=0 python run_mlm.py     --model_name_or_path bert-base-multilingual-uncased     --train_file /path/to/train.txt     --validation_file /path/to/validation.txt     --do_train     --do_eval     --output_dir /path/to/new/model/directory     --line_by_line     --eval_steps 2500     --save_total_limit 10     --save_steps 10 --logging_steps 2500 --max_steps 250000    --load_best_model_at_end    --per_device_train_batch_size 4     --gradient_accumulation_steps 2 --metric_for_best_model eval_loss --evaluation_strategy epoch --response_masking --mlm_probability 1.0

