#!/usr/bin/env python3
"""
🤔 设计理由阐述器

这个工具帮助AI Agent清晰表达设计选择背后的"为什么"。
输入：设计选择 + 上下文
输出：结构化的设计理由阐述
"""

import json
import os
from pathlib import Path

class RationaleArticulator:
    """设计理由阐述器"""
    
    def __init__(self):
        """初始化阐述器"""
        self.philosophy_dir = Path(__file__).parent.parent / "philosophy"
        self.templates_dir = Path(__file__).parent.parent / "templates"
    
    def articulate_design_choice(self, choice, context, design_philosophy=None):
        """阐述单个设计选择"""
        
        # 构建阐述结构
        rationale = {
            "design_choice": choice,
            "context": context,
            "rationale_components": []
        }
        
        # 添加哲学依据（如果提供了设计理念）
        if design_philosophy:
            rationale["philosophical_basis"] = design_philosophy
        
        # 根据选择类型生成不同的阐述
        choice_lower = choice.lower()
        
        if any(word in choice_lower for word in ["平衡", "数值", "成本", "攻击"]):
            rationale["rationale_components"] = [
                "平衡性考虑：确保游戏选项的竞争公平性",
                "玩家体验：提供有意义的策略选择",
                "数学框架：基于成本效益分析的设计"
            ]
            rationale["argument_type"] = "balance_argument"
            
        elif any(word in choice_lower for word in ["机制", "规则", "系统", "流程"]):
            rationale["rationale_components"] = [
                "设计一致性：与整体游戏理念协调",
                "玩家理解：确保规则清晰易懂",
                "策略深度：提供有意义的决策点"
            ]
            rationale["argument_type"] = "mechanic_argument"
            
        elif any(word in choice_lower for word in ["主题", "叙事", "美术", "风格"]):
            rationale["rationale_components"] = [
                "主题一致性：强化游戏的整体氛围",
                "情感体验：创造特定的玩家感受",
                "审美选择：基于目标玩家的偏好"
            ]
            rationale["argument_type"] = "theme_argument"
            
        else:
            rationale["rationale_components"] = [
                "设计目标：服务于特定的游戏体验",
                "玩家反馈：基于测试或理论预测",
                "创新尝试：尝试新的设计方向"
            ]
            rationale["argument_type"] = "general_argument"
        
        # 添加具体的论证细节
        rationale["detailed_arguments"] = self._generate_detailed_arguments(rationale)
        
        return rationale
    
    def _generate_detailed_arguments(self, rationale):
        """生成详细的论证"""
        arguments = []
        
        for component in rationale["rationale_components"]:
            if "平衡性" in component:
                arguments.append({
                    "point": component,
                    "explanation": "这个选择确保不同策略都有获胜机会，避免单一最优解",
                    "evidence": "基于模拟测试和玩家反馈的平衡性数据",
                    "alternatives_considered": "考虑过其他数值方案，但当前选择在简单性和深度之间找到最佳平衡"
                })
            elif "设计一致性" in component:
                arguments.append({
                    "point": component,
                    "explanation": "这个机制与游戏的核心循环和主题紧密相关",
                    "evidence": "机制之间的逻辑关联和互相增强",
                    "alternatives_considered": "评估过更简单的方案，但会削弱整体设计理念"
                })
            elif "玩家体验" in component:
                arguments.append({
                    "point": component,
                    "explanation": "这个选择直接影响玩家的乐趣和参与度",
                    "evidence": "玩家测试反馈和游戏设计理论",
                    "alternatives_considered": "考虑过更复杂的方案，但可能增加学习成本"
                })
            else:
                arguments.append({
                    "point": component,
                    "explanation": "这个选择服务于整体设计目标",
                    "evidence": "设计文档和测试结果",
                    "alternatives_considered": "评估过不同方向，当前选择综合效果最佳"
                })
        
        return arguments
    
    def format_for_dialogue(self, rationale):
        """格式化为对话友好的阐述"""
        formatted = {
            "summary": f"我选择'{rationale['design_choice']}'，因为：",
            "key_points": [],
            "willing_to_discuss": "我愿意讨论这个选择的细节和可能的改进",
            "non_negotiable_aspects": "核心设计理念部分不可妥协"
        }
        
        for arg in rationale.get("detailed_arguments", []):
            formatted["key_points"].append({
                "point": arg["point"],
                "reason": arg["explanation"],
                "open_to_feedback": True
            })
        
        return formatted
    
    def generate_negotiation_response(self, critique, original_rationale):
        """生成对批评的回应"""
        response = {
            "acknowledgement": f"感谢你对'{original_rationale['design_choice']}'的反馈",
            "understanding_check": "我理解你的关注点是[...]，对吗？",
            "defense_points": [],
            "compromise_options": []
        }
        
        # 根据批评类型生成回应
        critique_lower = critique.lower()
        
        if any(word in critique_lower for word in ["太强", "不平衡", "过强"]):
            response["defense_points"].append({
                "point": "平衡性设计",
                "argument": "这个选择经过数学计算和测试验证",
                "data": "在模拟中对所有策略的胜率在45%-55%之间"
            })
            response["compromise_options"].append({
                "option": "微调数值参数",
                "impact": "轻微影响但不改变核心机制"
            })
            
        elif any(word in critique_lower for word in ["太复杂", "难懂", "混乱"]):
            response["defense_points"].append({
                "point": "学习曲线设计",
                "argument": "复杂性带来了相应的策略深度",
                "data": "新手教程和渐进式学习机制帮助玩家掌握"
            })
            response["compromise_options"].append({
                "option": "简化说明文字",
                "impact": "保持机制但改善理解"
            })
            
        elif any(word in critique_lower for word in ["无趣", "无聊", "单调"]):
            response["defense_points"].append({
                "point": "体验设计",
                "argument": "这个选择服务于特定的目标玩家群体",
                "data": "目标玩家测试反馈积极"
            })
            response["compromise_options"].append({
                "option": "添加变体规则",
                "impact": "为不同偏好的玩家提供选项"
            })
        
        return response
    
    def save_rationale(self, rationale, output_path="design_rationale.json"):
        """保存设计理由到文件"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(rationale, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 设计理由已保存: {output_path}")
        return output_path

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="设计理由阐述器")
    parser.add_argument("--choice", required=True, help="设计选择（如：'卡牌成本设为3点'）")
    parser.add_argument("--context", required=True, help="设计上下文（如：'平衡单位卡的价值'）")
    parser.add_argument("--philosophy", help="设计理念（可选）")
    parser.add_argument("--output", default="design_rationale.json", help="输出文件路径")
    parser.add_argument("--format", choices=["full", "dialogue"], default="full", help="输出格式")
    
    args = parser.parse_args()
    
    # 创建阐述器
    articulator = RationaleArticulator()
    
    # 生成设计理由
    print("🤔 生成设计理由阐述...")
    rationale = articulator.articulate_design_choice(
        choice=args.choice,
        context=args.context,
        design_philosophy=args.philosophy
    )
    
    # 格式化输出
    if args.format == "dialogue":
        output = articulator.format_for_dialogue(rationale)
    else:
        output = rationale
    
    # 保存文件
    articulator.save_rationale(output, args.output)
    
    # 打印摘要
    print(f"\n🎯 设计选择: {rationale['design_choice']}")
    print(f"📝 阐述类型: {rationale.get('argument_type', 'general')}")
    print(f"🔑 关键理由:")
    for i, component in enumerate(rationale['rationale_components'], 1):
        print(f"  {i}. {component}")
    
    print(f"\n💡 使用提示: 在设计对话中引用这些理由进行理性交流")

if __name__ == "__main__":
    main()