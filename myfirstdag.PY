       task_id='generate_dataset',
        outlets=[my_dataset],
        bash_command='echo "data1,data2,data3\n" >> /tmp/data.csv',
    )

    check_file_task = BashOperator(
        task_id='check_file',
        bash_command='cat /tmp/data.csv',
    )

    generate_dataset >> check_file_task

# Define the consumer DAG
with DAG(dag_id='consumer_aware', 
        schedule = [my_dataset],
        start_date = datetime.now(),
        default_args=default_args) as dag:

    # Define the task that consumes the dataset
    consume_dataset = BashOperator(
        task_id="consume_dataset",
        bash_command="cat /tmp/data.csv",
        retries=3,
    )