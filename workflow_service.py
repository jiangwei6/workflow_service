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

        # 遍历 workflow，提取 task_id 和 inputs
        for task_id, task_data in workflow_data.items():
            if 'inputs' in task_data and isinstance(task_data['inputs'], dict):
                for input_key, input_value in task_data['inputs'].items():
                    # 过滤掉数组类型的值
                    if not isinstance(input_value, list):
                        result.append({
                            'task_id': task_id,
                            'inputs': input_key,
                            'default_value': input_value,
                            'class_type': task_data.get('class_type', 'Unknown'),
                            'ud_shuidegongzuoliu_my_comfyui_workflow_671649': 1
                        })

        # 返回结果
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
