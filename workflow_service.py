from flask import Flask, request, jsonify

app = Flask(__name__)

# 处理任务数据的 API
@app.route('/process', methods=['POST'])
def process_tasks():
    try:
        # 获取请求中的 JSON 数据，直接传递任务数据
        task_data = request.json

        # 初始化结果列表
        result = []

        # 遍历每个任务的 key 和 value
        for task_id, task_details in task_data.items():
            if 'inputs' in task_details and isinstance(task_details['inputs'], dict):
                for input_key, input_value in task_details['inputs'].items():
                    # 过滤掉数组类型的值2
                    if not isinstance(input_value, list):
                        result.append({
                            'task_id': task_id,
                            'inputs': input_key,
                            'default_value': input_value,
                            'class_type': task_details.get('class_type', 'Unknown'),
                            'ud_shuidegongzuoliu_my_comfyui_workflow_671649': 1
                        })

        # 返回结果2
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
