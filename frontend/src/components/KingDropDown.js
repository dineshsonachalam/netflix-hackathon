import React from 'react';
import { Select } from 'antd';
const { Option } = Select;

class KingDropDown extends React.Component {
      render() {
            function onChange(value) {
                console.log(`selected ${value}`);
            }
            
            function onBlur() {
                console.log('blur');
            }
            
            function onFocus() {
                console.log('focus');
            }
            
            function onSearch(val) {
                console.log('search:', val);
            }
            return (
                <div>
                    <Select
                        showSearch
                        style={{ width: 200 }}
                        placeholder="Select a person"
                        optionFilterProp="children"
                        onChange={onChange}
                        onFocus={onFocus}
                        onBlur={onBlur}
                        onSearch={onSearch}
                        filterOption={(input, option) =>
                        option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
                        }
                    >
                            <Option value="joffrey">Joffrey/Tommen Baratheon</Option>
                            <Option value="robb">Robb Stark</Option>
                            <Option value="balon">Balon/Euron Greyjoy</Option>
                            <Option value="stannis">Stannis Baratheon</Option>
                            <Option value="renly">Renly Baratheon</Option>
                    </Select>
                </div>
            );
      }
}

export default KingDropDown;


