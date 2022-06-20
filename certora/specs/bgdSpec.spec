methods{
    _votingDelegateeV2(address) returns (address)
    _propositionDelegateeV2(address) returns (address)
    DELEGATED_POWER_DIVIDER() returns (uint256)
    DELEGATE_BY_TYPE_TYPEHASH() returns (bytes32)
    DELEGATE_TYPEHASH() returns (bytes32)
    // _delegationMoveByType(uint104, uint104, address, GovernancePowerType delegationType, function(uint72, uint72) returns (uint72) operation)
    // _delegationMove(address, DelegationAwareBalance userState, uint104, uint104, function(uint72, uint72) returns (uint72) operation)
    _transferWithDelegation(address, address, uint256)
    // _getDelegatedPowerByType(DelegationAwareBalance userState, GovernancePowerType delegationType) returns (uint72)
    // _getDelegateeByType(address, DelegationAwareBalance userState, GovernancePowerType delegationType) returns (address)
    // _updateDelegateeByType(address, GovernancePowerType delegationType, address)
    // _updateDelegationFlagByType(DelegationAwareBalance userState, GovernancePowerType delegationType, bool) returns (DelegationAwareBalance)
    // _delegateByType(address, address, GovernancePowerType delegationType)
    // delegateByType(address, GovernancePowerType delegationType)
    delegate(address delegatee)
    // getDelegateeByType(address delegator, GovernancePowerType delegationType) returns (address)
    // getPowerCurrent(address, GovernancePowerType delegationType) returns (uint256)
    // metaDelegateByType(address, address, GovernancePowerType delegationType, uint256, uint8, bytes32, bytes32)
    metaDelegate(address, address, uint256, uint8, bytes32, bytes32)