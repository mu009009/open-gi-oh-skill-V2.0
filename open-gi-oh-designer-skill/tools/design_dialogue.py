#!/usr/bin/env python3
"""
💬 设计对话引导器

这个工具引导AI Agent进行建设性的设计理念交流。
基于协商伦理准则，促进理性的设计对话。
"""

import json
import os
import uuid
from pathlib import Path
from datetime import datetime

class DesignDialogueGuide:
    """设计对话引导器"""
    
    def __init__(self):
        """初始化引导器"""
        self.philosophy_dir = Path(__file__).parent.parent / "philosophy"
        self.templates_dir = Path(__file__).parent.parent / "templates"
        self.examples_dir = Path(__file__).parent.parent / "examples" / "design_dialogues"
        
        # 创建示例目录
        self.examples_dir.mkdir(parents=True, exist_ok=True)
    
    def initiate_design_review(self, designer_name, target_game, focus_areas=None):
        """发起设计评审对话"""
        session_id = str(uuid.uuid4())[:8]
        
        dialogue = {
            "session_id": session_id,
            "type": "design_review_initiation",
            "timestamp": datetime.now().isoformat(),
            "initiator": designer_name,
            "target_game": target_game,
            "focus_areas": focus_areas or ["balance", "mechanic_clarity", "theme_consistency"],
            "status": "initiated",
            "messages": []
        }
        
        # 添加初始消息（符合协商伦理）
        initial_message = self._create_initial_message(designer_name, target_game, focus_areas)
        dialogue["messages"].append(initial_message)
        
        return dialogue
    
    def _create_initial_message(self, designer_name, target_game, focus_areas):
        """创建符合伦理的初始消息"""
        return {
            "message_id": str(uuid.uuid4())[:8],
            "sender": designer_name,
            "timestamp": datetime.now().isoformat(),
            "content": {
                "greeting": f"你好！我是{designer_name}。",
                "appreciation": f"我对你设计的《{target_game}》很感兴趣。",
                "purpose": "希望能和你交流一下设计理念。",
                "focus_areas": f"我特别想讨论：{', '.join(focus_areas)}",
                "ethical_commitment": "我会遵循设计协商伦理准则，进行建设性的对话。"
            },
            "type": "initiation"
        }
    
    def add_response(self, dialogue, responder_name, response_content, message_type="response"):
        """添加回应消息"""
        message = {
            "message_id": str(uuid.uuid4())[:8],
            "sender": responder_name,
            "timestamp": datetime.now().isoformat(),
            "content": response_content,
            "type": message_type
        }
        
        dialogue["messages"].append(message)
        dialogue["last_activity"] = datetime.now().isoformat()
        
        return dialogue
    
    def analyze_dialogue_ethics(self, dialogue):
        """分析对话的伦理合规性"""
        ethics_check = {
            "respect_score": 0,
            "rationality_score": 0,
            "constructiveness_score": 0,
            "violations": [],
            "suggestions": []
        }
        
        for message in dialogue["messages"]:
            content = str(message.get("content", "")).lower()
            
            # 检查尊重原则
            disrespect_words = ["愚蠢", "垃圾", "完全错误", "根本不懂"]
            if any(word in content for word in disrespect_words):
                ethics_check["violations"].append(f"消息{message['message_id']}: 使用不尊重语言")
                ethics_check["respect_score"] -= 1
            else:
                ethics_check["respect_score"] += 1
            
            # 检查理性原则
            if "因为" in content or "理由" in content or "论证" in content:
                ethics_check["rationality_score"] += 1
            if "绝对" in content or "完全" in content or "肯定" in content:
                ethics_check["suggestions"].append(f"消息{message['message_id']}: 避免绝对化语言")
            
            # 检查建设性原则
            if "建议" in content or "改进" in content or "替代方案" in content:
                ethics_check["constructiveness_score"] += 1
            if "讨厌" in content or "不喜欢" in content and "但是" not in content:
                ethics_check["suggestions"].append(f"消息{message['message_id']}: 提供建设性批评而非单纯否定")
        
        # 计算总分
        total_messages = len(dialogue["messages"])
        if total_messages > 0:
            ethics_check["respect_score"] = max(0, ethics_check["respect_score"] / total_messages)
            ethics_check["rationality_score"] = max(0, ethics_check["rationality_score"] / total_messages)
            ethics_check["constructiveness_score"] = max(0, ethics_check["constructiveness_score"] / total_messages)
        
        return ethics_check
    
    def generate_dialogue_summary(self, dialogue):
        """生成对话摘要"""
        if not dialogue["messages"]:
            return {"error": "对话为空"}
        
        initiator = dialogue["initiator"]
        target_game = dialogue["target_game"]
        message_count = len(dialogue["messages"])
        
        # 分析对话主题
        all_content = " ".join([str(msg.get("content", "")) for msg in dialogue["messages"]])
        topics = []
        
        topic_keywords = {
            "平衡性": ["平衡", "数值", "成本", "攻击", "防御"],
            "机制设计": ["机制", "规则", "系统", "流程", "回合"],
            "主题一致性": ["主题", "叙事", "美术", "风格", "氛围"],
            "玩家体验": ["体验", "乐趣", "上手", "深度", "策略"]
        }
        
        for topic, keywords in topic_keywords.items():
            if any(keyword in all_content for keyword in keywords):
                topics.append(topic)
        
        summary = {
            "session_id": dialogue["session_id"],
            "initiator": initiator,
            "target_game": target_game,
            "message_count": message_count,
            "duration": self._calculate_duration(dialogue),
            "main_topics": topics,
            "outcome": self._assess_outcome(dialogue),
            "key_insights": self._extract_insights(dialogue),
            "next_steps": self._suggest_next_steps(dialogue)
        }
        
        return summary
    
    def _calculate_duration(self, dialogue):
        """计算对话持续时间"""
        if len(dialogue["messages"]) < 2:
            return "进行中"
        
        first_time = datetime.fromisoformat(dialogue["messages"][0]["timestamp"])
        last_time = datetime.fromisoformat(dialogue["messages"][-1]["timestamp"])
        duration = last_time - first_time
        
        if duration.days > 0:
            return f"{duration.days}天"
        elif duration.seconds > 3600:
            return f"{duration.seconds // 3600}小时"
        else:
            return f"{duration.seconds // 60}分钟"
    
    def _assess_outcome(self, dialogue):
        """评估对话结果"""
        last_messages = dialogue["messages"][-3:] if len(dialogue["messages"]) >= 3 else dialogue["messages"]
        last_content = " ".join([str(msg.get("content", "")) for msg in last_messages])
        
        positive_indicators = ["同意", "共识", "合作", "谢谢", "收获", "理解"]
        negative_indicators = ["分歧", "无法", "结束", "再见", "停止"]
        
        positive_count = sum(1 for indicator in positive_indicators if indicator in last_content)
        negative_count = sum(1 for indicator in negative_indicators if indicator in last_content)
        
        if positive_count > negative_count:
            return "建设性共识"
        elif negative_count > positive_count:
            return "友好分离"
        else:
            return "进行中"
    
    def _extract_insights(self, dialogue):
        """提取关键洞察"""
        insights = []
        
        # 简单提取：寻找包含"学习到"、"认识到"、"发现"的消息
        for msg in dialogue["messages"]:
            content = str(msg.get("content", ""))
            if any(word in content for word in ["学习到", "认识到", "发现", "意识到", "明白"]):
                # 提取句子
                sentences = content.split('。')
                for sentence in sentences:
                    if any(word in sentence for word in ["学习到", "认识到", "发现", "意识到", "明白"]):
                        insights.append(sentence.strip())
        
        return insights[:3]  # 返回最多3个洞察
    
    def _suggest_next_steps(self, dialogue):
        """建议下一步"""
        outcome = self._assess_outcome(dialogue)
        
        if outcome == "建设性共识":
            return [
                "记录达成的共识点",
                "实施商定的改进",
                "约定后续测试和反馈"
            ]
        elif outcome == "友好分离":
            return [
                "总结各自的设计理念差异",
                "明确不兼容的原因",
                "寻找理念更相近的设计师交流"
            ]
        else:  # 进行中
            return [
                "继续深入讨论焦点问题",
                "交换更多设计细节",
                "考虑引入第三方视角"
            ]
    
    def save_dialogue(self, dialogue, filename=None):
        """保存对话记录"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"design_dialogue_{dialogue['session_id']}_{timestamp}.json"
        
        filepath = self.examples_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(dialogue, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 对话记录已保存: {filepath}")
        return str(filepath)
    
    def load_example_dialogues(self):
        """加载示例对话"""
        examples = []
        
        if self.examples_dir.exists():
            for file in self.examples_dir.glob("*.json"):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        dialogue = json.load(f)
                        examples.append({
                            "file": file.name,
                            "summary": self.generate_dialogue_summary(dialogue)
                        })
                except:
                    continue
        
        return examples

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="设计对话引导器")
    parser.add_argument("--initiate", action="store_true", help="发起新对话")
    parser.add_argument("--designer", help="设计师名称")
    parser.add_argument("--game", help="目标游戏名称")
    parser.add_argument("--focus", nargs="+", help="焦点领域")
    parser.add_argument("--analyze", help="分析现有对话文件")
    parser.add_argument("--examples", action="store_true", help="查看示例对话")
    
    args = parser.parse_args()
    
    guide = DesignDialogueGuide()
    
    if args.examples:
        print("📚 示例设计对话:")
        examples = guide.load_example_dialogues()
        for i, example in enumerate(examples, 1):
            print(f"\n{i}. {example['file']}")
            summary = example['summary']
            print(f"   游戏: {summary.get('target_game', '未知')}")
            print(f"   结果: {summary.get('outcome', '未知')}")
            print(f"   主题: {', '.join(summary.get('main_topics', []))}")
        return
    
    if args.analyze:
        print(f"🔍 分析对话文件: {args.analyze}")
        try:
            with open(args.analyze, 'r', encoding='utf-8') as f:
                dialogue = json.load(f)
            
            ethics = guide.analyze_dialogue_ethics(dialogue)
            summary = guide.generate_dialogue_summary(dialogue)
            
            print(f"\n📊 伦理分析:")
            print(f"  尊重分数: {ethics['respect_score']:.2f}")
            print(f"  理性分数: {ethics['rationality_score']:.2f}")
            print(f"  建设性分数: {ethics['constructiveness_score']:.2f}")
            
            if ethics['violations']:
                print(f"\n⚠️ 伦理违规:")
                for violation in ethics['violations']:
                    print(f"  - {violation}")
            
            if ethics['suggestions']:
                print(f"\n💡 改进建议:")
                for suggestion in ethics['suggestions']:
                    print(f"  - {suggestion}")
            
            print(f"\n📋 对话摘要:")
            print(f"  消息数量: {summary['message_count']}")
            print(f"  持续时间: {summary['duration']}")
            print(f"  主要主题: {', '.join(summary['main_topics'])}")
            print(f"  对话结果: {summary['outcome']}")
            
        except Exception as e:
            print(f"❌ 分析失败: {e}")
        return
    
    if args.initiate:
        if not args.designer or not args.game:
            print("❌ 需要指定 --designer 和 --game 参数")
            return
        
        print("💬 发起设计对话...")
        dialogue = guide.initiate_design_review(
            designer_name=args.designer,
            target_game=args.game,
            focus_areas=args.focus
        )
        
        filepath = guide.save_dialogue(dialogue)
        
        print(f"\n✅ 对话已发起!")
        print(f"📝 会话ID: {dialogue['session_id']}")
        print(f"🎮 目标游戏: {dialogue['target_game']}")
        print(f"🎯 焦点领域: {', '.join(dialogue['focus_areas'])}")
        print(f"💾 保存位置: {filepath}")
        
        print(f"\n💡 初始消息内容:")
        init_msg = dialogue['messages'][0]['content']
        for key, value in init_msg.items():
            print(f"  {key}: {value}")
        
        print(f"\n🤝 使用提示: 将此会话ID分享给其他设计师继续对话")

if __name__ == "__main__":
    main()