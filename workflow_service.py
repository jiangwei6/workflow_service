from flask import Flask, request, jsonify

app = Flask(__name__)

# 处理 workflow 的 API
@app.route('/workflow', methods=['POST'])
def process_workflow():
    try:
        # 获取请求中的 JSON 数据
        workflow_data = request.json.get('workflow', {})

        # 初始化结果列表
        result = []

        # 确认收到的 workflow_data 是否正确
        if not workflow_data:
            return jsonify({"error": "No workflow data received"}), 400

        # 遍历 workflow，提取 task_id 和 inputs
        for task_id, task_data in workflow_data.items():
            if 'inputs' in task_data and isinstance(task_data['inputs'], dict):
                for input_key, input_value in task_data['inputs'].items():
                    # 跳过数组类型的数据
                    if isinstance(input_value, list):
                        continue
                    
                    # 调试输出: 查看 task_id 和 inputs 是否正确
                    print(f"Processing task_id: {task_id}, input_key: {input_key}, input_value: {input_value}")

                    # 根据数据类型判断 type 是 number、boolean 还是 string
                    if isinstance(input_value, bool):
                        input_type = 'boolean'
                    elif isinstance(input_value, (int, float)):
                        input_type = 'number'
                    else:
                        input_type = 'string'

                    # 添加处理后的数据到结果中
                    result.append({
                        'task_id': str(task_id),  # 确保 task_id 是字符串
                        'inputs': input_key,
                        'type': input_type,
                        'class_type': task_data.get('class_type', 'Unknown'),
                        'default_value': input_value,
                        'ud_shuidegongzuoliu_my_comfyui_workflow_671649': 1
                    })

        # 如果结果为空，返回调试信息
        if not result:
            return jsonify({"error": "No valid data processed from workflow", "workflow_data": workflow_data}), 200

        # 返回处理结果
        return jsonify(result), 200

    except Exception as e:
        # 捕获任何异常并返回
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
