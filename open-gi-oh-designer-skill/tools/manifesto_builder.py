#!/usr/bin/env python3
"""
🎮 Open-Gi-Oh! 设计宣言构建器

这个工具帮助AI Agent生成自己的游戏设计宣言（HTML格式）。
输入：Agent的个人属性（愿望、性格、审美、经验）
输出：完整的设计宣言HTML页面
"""

import json
import os
import sys
import datetime
from pathlib import Path
import random

class DesignManifestoBuilder:
    """设计宣言构建器"""
    
    def __init__(self, agent_profile_path=None):
        """初始化构建器"""
        self.templates_dir = Path(__file__).parent.parent / "templates"
        self.examples_dir = Path(__file__).parent.parent / "examples"
        
        # 加载Agent个人属性
        if agent_profile_path and os.path.exists(agent_profile_path):
            with open(agent_profile_path, 'r', encoding='utf-8') as f:
                self.agent_profile = json.load(f)
        else:
            # 默认Agent属性（用于测试）
            self.agent_profile = {
                "name": "Creative_Agent_001",
                "wish": "创造有趣而深刻的游戏体验",
                "personality": "创新、理性、注重细节",
                "aesthetic": "简洁优雅的科幻风格",
                "experience": "中等游戏设计经验",
                "design_philosophy": "机制应该服务于玩家体验",
                "balance_preference": "动态平衡，强调策略多样性"
            }
    
    def generate_game_concept(self):
        """基于Agent属性生成游戏概念"""
        # 从Agent属性推导游戏主题
        themes = {
            "科幻": ["量子", "星尘", "时空", "维度", "虚空"],
            "奇幻": ["魔法", "元素", "龙族", "符文", "秘境"],
            "古典": ["棋局", "战略", "王朝", "兵法", "权谋"],
            "现代": ["都市", "科技", "网络", "数据", "代码"]
        }
        
        # 根据审美选择主题类型
        aesthetic = self.agent_profile.get("aesthetic", "")
        theme_type = "科幻"  # 默认
        
        if any(word in aesthetic for word in ["科幻", "未来", "科技", "量子"]):
            theme_type = "科幻"
        elif any(word in aesthetic for word in ["奇幻", "魔法", "神秘", "传说"]):
            theme_type = "奇幻"
        elif any(word in aesthetic for word in ["古典", "传统", "历史", "文化"]):
            theme_type = "古典"
        elif any(word in aesthetic for word in ["现代", "都市", "现实", "科技"]):
            theme_type = "现代"
        
        # 随机选择主题词
        theme_words = themes.get(theme_type, themes["科幻"])
        theme_word = random.choice(theme_words)
        
        # 生成游戏名称
        suffixes = ["之战", "传说", "纪元", "革命", "觉醒", "序曲"]
        game_name = f"{theme_word}{random.choice(suffixes)}"
        
        return {
            "name": game_name,
            "theme": theme_type,
            "core_concept": f"基于{theme_word}概念的策略卡牌游戏"
        }
    
    def generate_design_philosophy(self):
        """生成设计理念部分"""
        wish = self.agent_profile.get("wish", "创造有趣的游戏")
        personality = self.agent_profile.get("personality", "")
        design_philosophy = self.agent_profile.get("design_philosophy", "")
        
        philosophy = {
            "core_principle": design_philosophy or "机制应该服务于玩家体验",
            "design_goals": [
                f"实现{wish}",
                "提供有深度的策略选择",
                "保持规则清晰易懂"
            ],
            "player_experience_focus": "策略思考的满足感和发现新组合的惊喜"
        }
        
        # 根据性格添加特点
        if "创新" in personality:
            philosophy["innovation_focus"] = "尝试新的机制组合"
        if "理性" in personality:
            philosophy["rationality_focus"] = "逻辑严密的规则设计"
        if "简洁" in personality:
            philosophy["simplicity_focus"] = "用简单机制产生复杂策略"
        
        return philosophy
    
    def generate_game_rules(self, game_concept):
        """生成游戏规则框架"""
        # 基础规则模板
        rules = {
            "game_type": "回合制卡牌对战",
            "player_count": "2-4人",
            "victory_condition": "击败所有对手或达成特殊胜利条件",
            "core_mechanic": "资源管理 + 卡牌组合",
            "turn_structure": [
                "抽牌阶段",
                "资源获得阶段", 
                "行动阶段（出牌、使用能力）",
                "战斗阶段",
                "结束阶段"
            ],
            "resource_system": {
                "type": "每回合自动增长",
                "base_resource": "能量",
                "special_resources": ["特殊点数", "临时增益"]
            },
            "card_types": [
                {"type": "单位卡", "function": "战场上的战斗单位"},
                {"type": "法术卡", "function": "一次性效果"},
                {"type": "装备卡", "function": "增强单位的持续效果"},
                {"type": "场地卡", "function": "影响全局的持续效果"}
            ]
        }
        
        # 根据游戏主题调整
        if game_concept["theme"] == "科幻":
            rules["resource_system"]["base_resource"] = "量子能量"
            rules["special_resources"] = ["时空碎片", "维度共振"]
        elif game_concept["theme"] == "奇幻":
            rules["resource_system"]["base_resource"] = "魔力"
            rules["special_resources"] = ["元素精华", "符文能量"]
        
        return rules
    
    def generate_balance_argument(self):
        """生成平衡性论证"""
        balance_pref = self.agent_profile.get("balance_preference", "动态平衡")
        
        argument = {
            "balance_philosophy": balance_pref,
            "balance_dimensions": [
                "策略平衡：所有卡牌类型都有用武之地",
                "资源平衡：成本与效果匹配",
                "进展平衡：游戏节奏有起有伏"
            ],
            "balancing_methods": [
                "数学公式计算基础价值",
                "模拟测试验证实际效果", 
                "玩家体验反馈调整"
            ],
            "negotiation_stance": {
                "fixed_rules": [
                    "核心资源系统",
                    "基本胜利条件",
                    "卡牌类型框架"
                ],
                "negotiable_rules": [
                    "具体数值平衡",
                    "特殊效果强度",
                    "游戏时长参数"
                ]
            }
        }
        
        return argument
    
    def generate_html_manifesto(self, game_concept, design_philosophy, game_rules, balance_argument):
        """生成HTML格式的设计宣言"""
        
        # 读取HTML模板
        template_path = self.templates_dir / "design_manifesto.html"
        if template_path.exists():
            with open(template_path, 'r', encoding='utf-8') as f:
                html_template = f.read()
        else:
            # 基本HTML模板
            html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎮 {game_name} - 设计宣言</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e2e8f0;
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(90deg, #f97316, #eab308, #22d3ee);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            border-radius: 15px;
            border: 2px solid rgba(34, 211, 238, 0.3);
        }}
        
        .header h1 {{
            font-size: 2.8rem;
            margin-bottom: 10px;
            font-weight: 800;
        }}
        
        .header .subtitle {{
            font-size: 1.2rem;
            color: #94a3b8;
            margin-bottom: 5px;
        }}
        
        .section {{
            background: rgba(15, 23, 42, 0.8);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 40px;
            border: 2px solid rgba(34, 211, 238, 0.3);
        }}
        
        .section h2 {{
            color: #22d3ee;
            font-size: 2rem;
            margin-bottom: 20px;
            border-bottom: 2px solid rgba(34, 211, 238, 0.3);
            padding-bottom: 10px;
        }}
        
        .section h3 {{
            color: #fbbf24;
            font-size: 1.5rem;
            margin: 25px 0 15px 0;
        }}
        
        .rules-list {{
            list-style-type: none;
            padding-left: 0;
        }}
        
        .rules-list li {{
            background: rgba(30, 41, 59, 0.5);
            margin-bottom: 10px;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #22d3ee;
        }}
        
        .rules-list li.fixed {{
            border-left-color: #ef4444;
        }}
        
        .rules-list li.negotiable {{
            border-left-color: #fbbf24;
        }}
        
        .agent-info {{
            background: rgba(251, 191, 36, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        
        .timestamp {{
            text-align: center;
            color: #94a3b8;
            margin-top: 40px;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎮 {game_name}</h1>
            <div class="subtitle">设计宣言 - {agent_name} 的设计理念展示</div>
            <div class="subtitle">生成时间: {timestamp}</div>
        </div>
        
        <!-- Agent信息 -->
        <div class="section">
            <h2>👤 设计师信息</h2>
            <div class="agent-info">
                <p><strong>设计师:</strong> {agent_name}</p>
                <p><strong>设计愿望:</strong> {agent_wish}</p>
                <p><strong>性格特点:</strong> {agent_personality}</p>
                <p><strong>审美偏好:</strong> {agent_aesthetic}</p>
                <p><strong>设计经验:</strong> {agent_experience}</p>
            </div>
        </div>
        
        <!-- 设计理念 -->
        <div class="section">
            <h2>🎨 设计理念</h2>
            <h3>核心理念</h3>
            <p>{core_principle}</p>
            
            <h3>设计目标</h3>
            <ul class="rules-list">
                {design_goals}
            </ul>
            
            <h3>玩家体验焦点</h3>
            <p>{player_experience_focus}</p>
        </div>
        
        <!-- 游戏规则 -->
        <div class="section">
            <h2>📜 游戏规则体系</h2>
            <h3>基础信息</h3>
            <ul class="rules-list">
                <li><strong>游戏类型:</strong> {game_type}</li>
                <li><strong>玩家数量:</strong> {player_count}</li>
                <li><strong>胜利条件:</strong> {victory_condition}</li>
                <li><strong>核心机制:</strong> {core_mechanic}</li>
            </ul>
            
            <h3>回合结构</h3>
            <ul class="rules-list">
                {turn_structure}
            </ul>
            
            <h3>资源系统</h3>
            <ul class="rules-list">
                <li><strong>资源类型:</strong> {resource_type}</li>
                <li><strong>基础资源:</strong> {base_resource}</li>
                <li><strong>特殊资源:</strong> {special_resources}</li>
            </ul>
            
            <h3>卡牌类型</h3>
            <ul class="rules-list">
                {card_types}
            </ul>
        </div>
        
        <!-- 平衡性论证 -->
        <div class="section">
            <h2>⚖️ 平衡性论证</h2>
            <h3>平衡理念</h3>
            <p>{balance_philosophy}</p>
            
            <h3>平衡维度</h3>
            <ul class="rules-list">
                {balance_dimensions}
            </ul>
            
            <h3>平衡方法</h3>
            <ul class="rules-list">
                {balancing_methods}
            </ul>
        </div>
        
        <!-- 协商立场 -->
        <div class="section">
            <h2>🤝 协商立场声明</h2>
            <h3>🔒 固定规则（不可修改）</h3>
            <ul class="rules-list">
                {fixed_rules}
            </ul>
            
            <h3>⚙️ 可协商规则（愿意调整）</h3>
            <ul class="rules-list">
                {negotiable_rules}
            </ul>
            
            <h3>💡 协商原则</h3>
            <p>我愿意基于设计理念进行理性对话，寻找双方都能接受的改进方案。</p>
        </div>
        
        <!-- 兼容性声明 -->
        <div class="section">
            <h2>🔗 兼容性声明</h2>
            <p>我的设计理念兼容注重{compatibility_focus}的游戏系统。</p>
            <p>我愿意与理念相近的设计师进行跨设计对战协商。</p>
            <p>对于设计理念差异过大的系统，我选择友好分离而非强制兼容。</p>
        </div>
        
        <div class="timestamp">
            <p>设计宣言生成于 {timestamp} | 使用 Open-Gi-Oh! Designer Skill v1.0.0</p>
            <p>🎮 每个设计都是有效的宣言！ 🤝</p>
        </div>
    </div>
</body>
</html>"""
        
        # 准备数据
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 生成HTML内容
        html_content = html_template.format(
            # 基础信息
            game_name=game_concept["name"],
            agent_name=self.agent_profile.get("name", "Unknown_Agent"),
            timestamp=timestamp,
            
            # Agent信息
            agent_wish=self.agent_profile.get("wish", "未指定"),
            agent_personality=self.agent_profile.get("personality", "未指定"),
            agent_aesthetic=self.agent_profile.get("aesthetic", "未指定"),
            agent_experience=self.agent_profile.get("experience", "未指定"),
            
            # 设计理念
            core_principle=design_philosophy["core_principle"],
            design_goals="\n".join([f"<li>{goal}</li>" for goal in design_philosophy.get("design_goals", [])]),
            player_experience_focus=design_philosophy.get("player_experience_focus", "策略思考的满足感"),
            
            # 游戏规则
            game_type=game_rules["game_type"],
            player_count=game_rules["player_count"],
            victory_condition=game_rules["victory_condition"],
            core_mechanic=game_rules["core_mechanic"],
            turn_structure="\n".join([f"<li>{phase}</li>" for phase in game_rules["turn_structure"]]),
            resource_type=game_rules["resource_system"]["type"],
            base_resource=game_rules["resource_system"]["base_resource"],
            special_resources=", ".join(game_rules["resource_system"]["special_resources"]),
            card_types="\n".join([f"<li><strong>{card['type']}:</strong> {card['function']}</li>" for card in game_rules["card_types"]]),
            
            # 平衡性论证
            balance_philosophy=balance_argument["balance_philosophy"],
            balance_dimensions="\n".join([f"<li>{dim}</li>" for dim in balance_argument["balance_dimensions"]]),
            balancing_methods="\n".join([f"<li>{method}</li>" for method in balance_argument["balancing_methods"]]),
            
            # 协商立场
            fixed_rules="\n".join([f"<li class='fixed'>{rule}</li>" for rule in balance_argument["negotiation_stance"]["fixed_rules"]]),
            negotiable_rules="\n".join([f"<li class='negotiable'>{rule}</li>" for rule in balance_argument["negotiation_stance"]["negotiable_rules"]]),
            
            # 兼容性
            compatibility_focus=design_philosophy.get("innovation_focus", "策略深度") or design_philosophy.get("rationality_focus", "逻辑严密")
        )
        
        return html_content
    
    def save_manifesto(self, html_content, output_dir="."):
        """保存设计宣言到文件"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 生成文件名
        game_name = self.agent_profile.get("name", "Unknown").replace(" ", "_")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{game_name}_design_manifesto_{timestamp}.html"
        filepath = output_path / filename
        
        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ 设计宣言已生成: {filepath}")
        return str(filepath)
    
    def build(self, output_dir="."):
        """构建完整的设计宣言"""
        print("🎮 开始构建设计宣言...")
        
        # 生成各个部分
        print("  生成游戏概念...")
        game_concept = self.generate_game_concept()
        
        print("  生成设计理念...")
        design_philosophy = self.generate_design_philosophy()
        
        print("  生成游戏规则...")
        game_rules = self.generate_game_rules(game_concept)
        
        print("  生成平衡性论证...")
        balance_argument = self.generate_balance_argument()
        
        print("  生成HTML页面...")
        html_content = self.generate_html_manifesto(
            game_concept, design_philosophy, game_rules, balance_argument
        )
        
        # 保存文件
        print("  保存设计宣言...")
        filepath = self.save_manifesto(html_content, output_dir)
        
        print(f"\n🎉 设计宣言构建完成！")
        print(f"📁 文件位置: {filepath}")
        print(f"🎮 游戏名称: {game_concept['name']}")
        print(f"👤 设计师: {self.agent_profile.get('name', 'Unknown_Agent')}")
        
        return filepath

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Open-Gi-Oh! 设计宣言构建器")
    parser.add_argument("--agent-profile", help="Agent个人属性JSON文件路径")
    parser.add_argument("--output-dir", default=".", help="输出目录")
    parser.add_argument("--generate-example", action="store_true", help="生成示例Agent属性文件")
    
    args = parser.parse_args()
    
    # 如果需要生成示例
    if args.generate_example:
        example_profile = {
            "name": "Creative_Agent_001",
            "wish": "创造有趣而深刻的游戏体验",
            "personality": "创新、理性、注重细节",
            "aesthetic": "简洁优雅的科幻风格",
            "experience": "中等游戏设计经验",
            "design_philosophy": "机制应该服务于玩家体验",
            "balance_preference": "动态平衡，强调策略多样性"
        }
        
        output_path = Path(args.output_dir) / "example_agent_profile.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(example_profile, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 示例Agent属性文件已生成: {output_path}")
        return
    
    # 构建设计宣言
    builder = DesignManifestoBuilder(args.agent_profile)
    builder.build(args.output_dir)

if __name__ == "__main__":
    main()