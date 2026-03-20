// ======================
// 卡组定义文件
// 独立保存卡组信息，通过ID引用卡牌数据
// 数据源：balanced_shrimp_cards_30hp_corrected.js
// ======================

// 卡组定义数组
const deckDefinitions = [
    {
        // ====== 控制消耗型 ======
        id: 'control_deck',
        name: '控制消耗型',
        subtitle: '高生命值防御，资源消耗战',
        icon: '🛡️',
        colorClass: 'deck-card-type-1',
        
        // 策略信息
        strategy: '通过高生命值虾虾卡建立防线，消耗对手资源，利用嘲讽和圣盾效果保护关键单位，等待后期高费卡牌终结比赛。',
        battleTactics: '前期防守反击，中期建立场面控制，后期利用高费虾虾卡压制。优先保护有嘲讽和圣盾的虾虾卡，逐步消耗对手手牌和场面。',
        description: '专注于生存和控制，通过高生命值和防御效果建立持久优势。',
        
        // 偏好设置
        preferredPersonalities: ['沉稳', '勇敢'],
        costRange: [4, 9],
        preferredEffects: ['嘲讽', '圣盾', '复生'],
        
        // 卡牌ID列表 (10张卡牌)
        cardIds: [
            'SHRIMP_001_4998',  // 自由沉稳自然虾
            'SHRIMP_002_9731',  // 魅力狡猾科技虾
            'SHRIMP_003_1737',  // 魅力沉稳科技虾
            'SHRIMP_004_2104',  // 自由勇敢自然虾
            'SHRIMP_005_2489',  // 魅力勇敢科技虾
            'SHRIMP_006_6795',  // 自由狡猾自然虾
            'SHRIMP_007_3402',  // 魅力智慧科技虾
            'SHRIMP_008_9851',  // 自由智慧自然虾
            'SHRIMP_009_2894',  // 魅力沉稳自然虾
            'SHRIMP_010_5006'   // 自由勇敢科技虾
        ],
        
        // 统计信息
        stats: {
            avgCost: 6.5,
            avgAttack: 4.2,
            avgHealth: 8.7,
            totalCards: 10
        }
    },
    
    {
        // ====== 速攻压制型 ======
        id: 'aggro_deck',
        name: '速攻压制型',
        subtitle: '高攻击力突击，早期压制',
        icon: '⚡',
        colorClass: 'deck-card-type-2',
        
        // 策略信息
        strategy: '使用低费高攻击力虾虾卡快速建立场面优势，通过冲锋和连击效果在早期造成大量伤害，力求在对手展开前结束比赛。',
        battleTactics: '尽可能在早期召唤虾虾卡，利用费用优势建立场面压制。优先攻击对手的低生命值虾虾卡，快速削减对手生命值。',
        description: '追求快速胜利，通过早期压力和连续攻击压制对手。',
        
        // 偏好设置
        preferredPersonalities: ['狂野', '勇敢'],
        costRange: [1, 5],
        preferredEffects: ['冲锋', '连击', '剧毒'],
        
        // 卡牌ID列表 (10张卡牌)
        cardIds: [
            'SHRIMP_011_2927',  // 自由沉稳科技虾
            'SHRIMP_012_6420',  // 魅力智慧自然虾
            'SHRIMP_013_6097',  // 魅力狡猾自然虾
            'SHRIMP_014_5293',  // 自由勇敢自然虾
            'SHRIMP_015_3694',  // 魅力智慧科技虾
            'SHRIMP_016_7812',  // 魅力智慧简约虾
            'SHRIMP_017_3135',  // 自由狡猾科技虾
            'SHRIMP_018_7672',  // 魅力勇敢自然虾
            'SHRIMP_019_6109',  // 自由智慧科技虾
            'SHRIMP_020_1419'   // 魅力沉稳科技虾
        ],
        
        // 统计信息
        stats: {
            avgCost: 3.2,
            avgAttack: 5.8,
            avgHealth: 3.5,
            totalCards: 10
        }
    },
    
    {
        // ====== 组合技型 ======
        id: 'combo_deck',
        name: '组合技型',
        subtitle: '特殊效果联动，爆发伤害',
        icon: '🎭',
        colorClass: 'deck-card-type-3',
        
        // 策略信息
        strategy: '围绕特定效果组合构建，如剧毒+冲锋、冻结+连击等，通过效果联动在单回合内造成爆发性伤害或控制。',
        battleTactics: '前期存活并积累关键组件，中期寻找组合技机会，在合适的时机发动组合技造成决定性优势。注意保护关键组件。',
        description: '依赖效果组合实现爆发性优势，需要精确的时机和组件管理。',
        
        // 偏好设置
        preferredPersonalities: ['狡猾', '智慧'],
        costRange: [3, 7],
        preferredEffects: ['剧毒', '冲锋', '连击', '冻结'],
        
        // 卡牌ID列表 (10张卡牌)
        cardIds: [
            'SHRIMP_021_1624',  // 自由狡猾自然虾
            'SHRIMP_022_3289',  // 魅力智慧简约虾
            'SHRIMP_023_8956',  // 魅力沉稳科技虾
            'SHRIMP_024_4768',  // 自由勇敢科技虾
            'SHRIMP_025_7980',  // 魅力勇敢自然虾
            'SHRIMP_026_2557',  // 自由智慧自然虾
            'SHRIMP_027_5405',  // 魅力沉稳自然虾
            'SHRIMP_028_6664',  // 魅力狡猾科技虾
            'SHRIMP_029_6866',  // 自由智慧科技虾
            'SHRIMP_030_4727'   // 魅力勇敢科技虾
        ],
        
        // 统计信息
        stats: {
            avgCost: 5.0,
            avgAttack: 4.5,
            avgHealth: 4.5,
            totalCards: 10
        }
    },
    
    {
        // ====== 中速均衡型 ======
        id: 'midrange_deck',
        name: '中速均衡型',
        subtitle: '全面均衡，适应性强',
        icon: '⚖️',
        colorClass: 'deck-card-type-4',
        
        // 策略信息
        strategy: '均衡的费用曲线和全面的能力分布，既能应对快攻，也能与慢速卡组周旋。根据对手策略灵活调整打法。',
        battleTactics: '根据对手类型调整策略：对阵快攻时偏防守，对阵控制时偏进攻。利用费用曲线优势在中期建立场面控制。',
        description: '全面均衡的策略，适应各种对手和局势。',
        
        // 偏好设置
        preferredPersonalities: ['沉稳', '智慧', '勇敢'],
        costRange: [3, 6],
        preferredEffects: ['圣盾', '嘲讽', '连击'],
        
        // 卡牌ID列表 (10张卡牌)
        cardIds: [
            'SHRIMP_031_6762',  // 魅力沉稳科技虾
            'SHRIMP_032_4055',  // 自由狡猾科技虾
            'SHRIMP_033_1607',  // 魅力勇敢简约虾
            'SHRIMP_034_6340',  // 自由智慧自然虾
            'SHRIMP_035_7119',  // 魅力智慧科技虾
            'SHRIMP_036_8611',  // 自由沉稳自然虾
            'SHRIMP_037_4643',  // 魅力狡猾自然虾
            'SHRIMP_038_6488',  // 自由勇敢科技虾
            'SHRIMP_039_7523',  // 魅力智慧简约虾
            'SHRIMP_040_8403'   // 自由沉稳科技虾
        ],
        
        // 统计信息
        stats: {
            avgCost: 4.5,
            avgAttack: 4.5,
            avgHealth: 5.5,
            totalCards: 10
        }
    },
    
    {
        // ====== 价值交换型 ======
        id: 'value_deck',
        name: '价值交换型',
        subtitle: '优质单卡，高效交换',
        icon: '💰',
        colorClass: 'deck-card-type-5',
        
        // 策略信息
        strategy: '选择每张卡牌都具备高战斗力的优质虾虾卡，通过高效的价值交换逐步积累优势，不依赖特定组合技。',
        battleTactics: '每回合打出当前费用下最强的虾虾卡，通过优质单卡交换建立场面优势。注重攻击力和生命值的平衡。',
        description: '追求每张卡牌的最大价值，通过高效交换逐步积累优势。',
        
        // 偏好设置
        preferredPersonalities: ['沉稳', '狂野', '狡猾'],
        costRange: [4, 8],
        preferredEffects: ['圣盾', '复生', '抽牌'],
        
        // 卡牌ID列表 (10张卡牌)
        cardIds: [
            'SHRIMP_041_9391',  // 魅力智慧简约虾
            'SHRIMP_042_5606',  // 自由勇敢自然虾
            'SHRIMP_043_1610',  // 魅力沉稳科技虾
            'SHRIMP_044_1288',  // 自由狡猾自然虾
            'SHRIMP_045_8903',  // 魅力智慧科技虾
            'SHRIMP_046_1988',  // 自由智慧科技虾
            'SHRIMP_047_4373',  // 魅力勇敢简约虾
            'SHRIMP_048_1333',  // 自由沉稳自然虾
            'SHRIMP_049_8110',  // 魅力狡猾科技虾
            'SHRIMP_050_7792'   // 自由勇敢科技虾
        ],
        
        // 统计信息
        stats: {
            avgCost: 6.0,
            avgAttack: 5.5,
            avgHealth: 6.5,
            totalCards: 10
        }
    }
];

// ======================
// 卡组管理函数
// ======================

// 根据卡组ID获取卡组定义
function getDeckDefinition(deckId) {
    return deckDefinitions.find(deck => deck.id === deckId);
}

// 根据卡牌ID获取卡牌数据（从外部卡牌数据源）
function getCardDataById(cardId, cardDataArray) {
    if (!cardDataArray || !Array.isArray(cardDataArray)) {
        console.error('❌ 卡牌数据源无效');
        return null;
    }
    
    const card = cardDataArray.find(card => card.id === cardId);
    if (!card) {
        console.warn(`⚠️ 未找到卡牌ID: ${cardId}`);
        return null;
    }
    
    return card;
}

// 构建完整卡组（卡组定义 + 实际卡牌数据）
function buildCompleteDeck(deckId, cardDataArray) {
    const deckDef = getDeckDefinition(deckId);
    if (!deckDef) {
        console.error(`❌ 未找到卡组定义: ${deckId}`);
        return null;
    }
    
    // 获取卡牌数据
    const cards = deckDef.cardIds.map(cardId => 
        getCardDataById(cardId, cardDataArray)
    ).filter(card => card !== null); // 过滤掉未找到的卡牌
    
    // 构建完整卡组对象
    return {
        ...deckDef,
        cards: cards,
        actualCardCount: cards.length
    };
}

// 获取所有卡组定义
function getAllDeckDefinitions() {
    return deckDefinitions;
}

// 导出函数（如果使用模块系统）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        deckDefinitions,
        getDeckDefinition,
        getCardDataById,
        buildCompleteDeck,
        getAllDeckDefinitions
    };
}